from django.db import models
from datetime import date
from decimal import Decimal
import re
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


def validate_iban(value):
    # IBAN format regex (this is a basic example, you may need to adjust it for specific country formats)
    iban_regex = r'^[A-Z]{2}[0-9]{2}[A-Z0-9]{4,30}$'
    
    if not re.match(iban_regex, value):
        raise ValidationError('Invalid IBAN format.')
    
def validate_fee_percentage(value):
    if value > 100:
        raise ValidationError('Fee percentage cannot exceed 100%.')
    
class Investor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True,validators=[EmailValidator()])
    iban = models.CharField(max_length=34,validators=[validate_iban] )
    amount_invested = models.DecimalField(max_digits=10, decimal_places=2)  # Investment amount for calculations
    investment_date = models.DateField()  # Added investment date for yearly fee calculations

    def __str__(self):
        return self.name

class Bill(models.Model):
    BILL_TYPES = [
        ('membership', 'Membership'),
        ('upfront', 'Upfront Fee'),
        ('yearly', 'Yearly Fee')
    ]
    investor = models.ForeignKey(Investor, related_name='bills', on_delete=models.CASCADE)
    bill_type = models.CharField(choices=BILL_TYPES, max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  # Non-editable amount field
    due_date = models.DateField()
    date_created = models.DateField(auto_now_add=True)
    fee_percentage = models.DecimalField(max_digits=5, decimal_places=3, default=Decimal('0.0'),validators=[validate_fee_percentage])  # Default fee percentage

    def save(self, *args, **kwargs):
        # Calculate the amount based on bill type
        if self.bill_type == 'membership':
            self.fee_percentage = Decimal('0')
            self.calculate_membership()
        elif self.bill_type == 'upfront':
            self.calculate_upfront_fee()
        elif self.bill_type == 'yearly':
            self.calculate_yearly_fee()
        super().save(*args, **kwargs)

    def calculate_membership(self):
        # Membership fee is 3000 EUR per year if amount invested is <= 50,000
        self.amount = Decimal('3000') if self.investor.amount_invested <= Decimal('50000') else Decimal('0')

    def calculate_upfront_fee(self):
        # Upfront fee = (fee percentage) x (amount invested) x 5 years
        self.amount = self.fee_percentage * self.investor.amount_invested * Decimal('5')

    def calculate_yearly_fee(self):
        investment_date = self.investor.investment_date
        current_year = date.today().year
        years_since_investment = current_year - investment_date.year
        fee_percentage = self.fee_percentage

        if years_since_investment == 0:
            # First year calculation based on days active in the year
            days_in_year = 366 if investment_date.year % 4 == 0 else 365
            days_active = (date.today() - investment_date).days
            self.amount = (Decimal(days_active) / Decimal(days_in_year)) * fee_percentage * self.investor.amount_invested
        elif years_since_investment == 1:
            self.amount = fee_percentage * self.investor.amount_invested
        elif years_since_investment == 2:
            self.amount = (fee_percentage - Decimal('0.002')) * self.investor.amount_invested
        elif years_since_investment == 3:
            self.amount = (fee_percentage - Decimal('0.005')) * self.investor.amount_invested
        else:
            self.amount = (fee_percentage - Decimal('0.01')) * self.investor.amount_invested

    def __str__(self):
        return f"{self.bill_type} - {self.amount} for {self.investor.name}"


class CapitalCall(models.Model):
    STATUS_CHOICES = [
        ('validated', 'Validated'),
        ('sent', 'Sent'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue')
    ]
    investor = models.ForeignKey(Investor, related_name='capital_calls', on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, editable=False)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    date = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    def save(self, *args, **kwargs):
        # Calculate total amount by summing related bills for the investor
        if self.total_amount is None:
            self.total_amount = sum(bill.amount for bill in self.investor.bills.all() if bill.amount)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Capital Call for {self.investor.name} - {self.status}"

    @property
    def investor_iban(self):
        # Access the IBAN from the related Investor model
        return self.investor.iban