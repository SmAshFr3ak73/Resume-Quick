from flask import Flask

app = Flask('/')
def home():
    return render_template('home.html')

app = Flask('/register/')
def register():
    return render_template('register.html')

app = Flask('/login/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)