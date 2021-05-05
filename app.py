'''
Refer:https://www.youtube.com/watch?v=bd5nsMscPo0
Refer:https://www.geeksforgeeks.org/reading-writing-text-files-python/
Refer:https://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto
Refer:https://www.youtube.com/watch?v=aojoWWMN1r0&t=1071s
'''
from flask import Flask
app = Flask(__name__)

from views import *

if __name__ == "__main__":
    app.run(debug="true")