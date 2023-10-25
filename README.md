# python-project_flask
Assignment for python flask learning

https://github02.hclpnp.com/storage/user/2187/files/b54c41fa-2723-4f9d-84ec-fa8049c1be10


# Flask Application README

This README provides instructions for running the Flask application that displays and sorts data from a "Devices" table.

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- Python 3
- pip (Python package manager)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-flask-app.git

cd your-flask-app

python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate  # Windows

pip install -r requirements.txt

Modify the config.py file to configure your database connection details:
SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://YourUsername:YourPassword@YourServer/YourDatabase?driver=ODBC+Driver+17+for+SQL+Server'
Replace YourUsername, YourPassword, YourServer, and YourDatabase with your actual database connection details.


# Running the Application
Initialize the database and populate it with sample data:
python init_db.py
---------------

Start the Flask application:
python app.py
-------------

Access the application in your web browser:
http://localhost:3000/

# Usage
The web page will display the data from the "Devices" table in a sortable table format.
Click on column headers to sort the data based on the selected column.



