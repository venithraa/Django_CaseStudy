# Capital Call Management System
This project provides an API and a simple frontend for managing capital calls and billing for investors in a private equity setting. Developed using Django REST Framework, it allows for the automation of invoice generation and capital call tracking, significantly reducing the manual workload.

# Problem
The company wishes to send invoices as part of the capital call to investors. This process is currently done manually with excel files and therefore it creates issue of redundancy as well as difficulties in maintenance of such excel files. Since, there are so many issues with the manual process, the company has decided to invest its resources towards building a product that automates this process of sending the invoices.

Capital Call :
A Capital call is an invoice we send to the user (in this example an investor). It groups a set of bills. There are many types of bills that can be created. One investor can have multiple bills. These bills need to be generated by a script/ command. Those generated bills will be stored to be checked by a human eye. The Human has the option to group them by investor. Once validated we need to generate an invoice and email the investor, this is the capital call. For the purposes of this business study, the generation of the invoice and sending of email are out of scope. We need to check the status of the cash call if it has been: validated, sent, paid or is overdue. Again, the process of receiving feedback from email servers or payment providers is out of scope from the perspective of this business case study.

Bill :
Since, we have talked already about the various types of bills. Therefore, underneath you find some possible bills. Although, the manner we calculate bills
is always changing over time depending upon various business reasons but, for the purposes of our problem, the following are the types of possible bills
• Membership
Active members need to pay a yearly subscription for using the platform. This is 3000 euro per year. In the event of an investor investing more than EUR
50000, he does not need to pay any of the yearly subscription.
• Upfront fees
The investor has the choice to pay all his fees upfront for an investment. So we can only bill him once for it
upfront fees = (fee percentage) x (amount invested) x 5 years
• Yearly fees
An investor can also pay his fees per year for an investment.
Please take into account the following information while designing your system-
Yearly fees before 2019/04
• First year:
Fees = (date of the investment bought / 365) x (fee percentage) x (amount
invested)
• Other years:
Fees = (fee percentage) x amount invested
Yearly fees after 2019/04
• First year:
Fees = date of the investment bought / amount days in that year x fee
percentage x amount invested
• Second year:
Fees = (fee percentage) x (amount invested)
• Third year:
Fees = (fee percentage - 0.20 %) x (amount invested)
• Fourth year:
Fees = (fee percentage - 0.50 %) x (amount invested)
• Following years:
Fees = (fee percentage - 1 %) x (amount invested)

# Features
1) Investor and bill management with various bill types: membership, upfront fees, and yearly fees.
2) Automatic bill calculations based on investment amounts, fee percentages, and investment duration.
3) Capital calls generation with options to group bills by investor and track status (validated, sent, paid, overdue).
4) Frontend interface built with HTML and Bootstrap for displaying investors, bills, and capital calls.

# Step-by-Step Installation
1) Clone the repository -- git clone git@github.com:venithraa/archimed_case_study.git
2) Create a virtual environment
3) Install the required dependencies -- pip install django djangorestframework
4) Run database migrations -- python manage.py migrate
6) Run the application -- python manage.py runserver

Now, the application should be running locally at http://127.0.0.1:8000 (frontend which displays results of the api)

# Usage
1) Running the App
The app will be available at http://127.0.0.1:8000/ by default. This provides the front-end interface for managing capital calls and investors.
![Screenshot 2024-11-13 015024](https://github.com/user-attachments/assets/5f873b6a-a886-41a9-a016-5bf1a90ca294)
![Screenshot 2024-11-13 015117](https://github.com/user-attachments/assets/18024344-d039-4e13-a8aa-5bac3fc250a2)


3) API endpoints are available at http://127.0.0.1:8000/api/ to allow CRUD operations on investors, bills, and capital calls.
![Screenshot 2024-11-13 014531](https://github.com/user-attachments/assets/9cec830c-a103-457d-8c5c-3be8e49b2bde)


-- API Endpoints
1) GET /api/investors/: Get a list of all investors.
2) POST /api/investors/: Create a new investor (requires name, email, iban, amount_invested, investment_date).
![Screenshot 2024-11-13 015215](https://github.com/user-attachments/assets/6ed87086-7ad1-4cf3-afae-221c14e4dc00)
![Screenshot 2024-11-13 015154](https://github.com/user-attachments/assets/e077f389-55ca-4bfa-ba05-d0d5a4960145)


4) GET /api/bills/: Get all bills for all investors.
5) POST /api/bills/: Create a new bill (requires investor, bill_type, due_date, fee_percentage).
![Screenshot 2024-11-13 015232](https://github.com/user-attachments/assets/a07ef3e5-45d6-4500-a750-116ab24ae08c)
![Screenshot 2024-11-13 015243](https://github.com/user-attachments/assets/04f7ccff-4988-4265-b5ca-7f1661527729)


7) GET /api/capital_calls/: Get all capital calls.
8) POST /api/capital_calls/: Create a new capital call (requires investor, status, due_date).
![Screenshot 2024-11-13 015312](https://github.com/user-attachments/assets/c1b9188c-96b5-45c9-97b1-a57954d03438)
![Screenshot 2024-11-13 015323](https://github.com/user-attachments/assets/d0ab9694-1413-4843-b901-d0565ece87dd)

# IBAN Validator (Asumptions)
This section explains the implementation of the IBAN (International Bank Account Number) validator used in the project. The IBAN is used to uniquely identify a bank account for international transactions.

Assumptions in the Code:
IBAN Structure:

The IBAN starts with a two-letter country code ([A-Z]{2}), followed by two check digits ([0-9]{2}).
The remainder of the IBAN ([A-Z0-9]{4,30}) consists of a combination of uppercase letters and numbers, which can vary in length from 4 to 30 characters, based on the country.
