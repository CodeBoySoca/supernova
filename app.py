from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from mongoframes import *
from models import *
import os

load_dotenv('.env')

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def homepage():
    assets = Asset.retrieve()
    return render_template('index.html', assets=assets)

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
    return render_template('portfolio.html')

@app.route('/messages')
def messages():
    return render_template('messages.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/asset/<id>')
def asset(id):
    return render_template('asset.html')







if __name__ == '__main__':
    app.run()