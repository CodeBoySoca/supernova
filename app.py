from flask import Flask, render_templates


app = Flask(__name__)


@app.route('/')
def homepage():
    pass

@app.route('/signup')
def signup():
    pass

@app.route('/signin')
def signin():
    pass

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