from rest_framework import serializers
from .models import Investor, Bill, CapitalCall

class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['investor', 'bill_type', 'due_date', 'fee_percentage', 'amount'] 
        read_only_fields = ['amount'] 

class CapitalCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapitalCall
        fields = ['investor', 'status', 'date', 'due_date', 'total_amount']  
        read_only_fields = ['total_amount']