#__init__.py where we initialize our application adn bring together differnet components
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)


'''
>>> import secrets
>>> secrets.token_hex(16)
'f8d1e7b246c52fd81b103f0e265294ca'
'''
# when we use these forms we need a secret key , a secret key will protect against modifiying cookies and cross-site request forgery attacks
app.config['SECRET_KEY'] = 'fac072214929018288a5d4c197bbf3f0'
# use random set of characters for secret key
# dummy data for rendering posts

# DATABASE_URL = 'mssql+pyodbc://myuser:mypassword@myserver/mydatabase?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc://sa:Viswafiza%4002@WIN-CFN9TN3HFBQ/dummy?driver=ODBC+Driver+17+for+SQL+Server"

db = SQLAlchemy(app)
print('db connected')
bcrypt = Bcrypt(app)
login_manager= LoginManager(app)

login_manager.login_view = 'login'
login_manager.login_message_category='info'

from devices import routes
