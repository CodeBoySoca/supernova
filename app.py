from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
import os

load_dotenv('.env')

app = Flask(__name__)
csrf = CSRFProtect(app)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/logout')
def logout():
    pass

@app.route('/portfolio')
def portfolio():
    pass

@app.route('/messages')
def messages():
    pass

@app.route('/account')
def account():
    pass









if __name__ == '__main__':
    app.run()