from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '634e6b75aa8af08e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='account.png')
    password = db.Column(db.String(60), nullable=False)

    def __init__(self, username, email, image_file):
        self.username = username
        self.email = email
        self.image_file = image_file

    def __repr__(self):
        return {'username':self.username, 'email':self.email, 'image_file':self.image_file}
    
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account successfully created!', 'sucess')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@test.com' and form.password.data == 'password':
            flash('Successful login!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Unsuccessful login. Check email and password!', 'danger')
    return render_template('login.html', form=form)

@app.route("/account")
def account():
    return render_template('account.html')

@app.route("/alerts")
def alerts():
    return render_template('alerts.html')

@app.route("/charts")
def charts():
    return render_template('charts.html')

@app.route("/wallet")
def wallet():
    return render_template('wallet.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
