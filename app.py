from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '634e6b75aa8af08e'

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {form.username.data}!', 'sucess')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/login")
def login():
    form = LoginForm()
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
