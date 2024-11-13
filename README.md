# Capital Call Management System
This project provides an API and a simple frontend for managing capital calls and billing for investors in a private equity setting. Developed using Django and Django REST Framework, it allows for the automation of invoice generation and capital call tracking, significantly reducing the manual workload.

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



# Frontend
The frontend is a basic HTML page with Bootstrap that allows you to view the details of:

1) Investors
2) Bills
3) Capital Calls
