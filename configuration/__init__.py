from app import app
import urllib
import os

# secret key for user session
app.secret_key = "ITSASECRET"

#setting up mail
app.config['MAIL_SERVER']='smtp.gmail.com' #mail server
app.config['MAIL_PORT'] = 587 #mail port
app.config['MAIL_USERNAME'] = 'r2singh.1306@gmail.com' #email
app.config['MAIL_PASSWORD'] = urllib.parse.quote('Erick@123') #password os.environ[
app.config['MAIL_USE_TLS'] = True #security type
app.config['MAIL_USE_SSL'] = False #security type

#database connection parameters
connection_params = { 
    'user': 'rohitgr8',
    'password': urllib.parse.quote('Erick@123'), #os.environ[
    'host': 'cluster0.lpjae.mongodb.net',
    'port': 8080,
    'namespace': 'userusers',
}
