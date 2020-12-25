from flask import Flask, render_template, abort, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '0342cf57e6fb58ee2634f555ab2485c2'


cows = [
    {"id": 1, "name": "Nandni", "age": "5 years",
     "story": "hdj  ajkf dakfj k lkfjlk fjlkajflka flkd flk dfj"},
    {"id": 2, "name": "CowNo2", "age": "8 months",
     "story": "djkfd jfklsdaj fdlkfj ldjfl;a df fk dlsfj"},
    {"id": 3, "name": "CowNo3", "age": "1 year", "story": "jf kajf kdjflajflkd : ("},
    {"id": 4, "name": "CowNo4", "age": "5 years", "story": " jk dajfl fj alf ;la"},
]


@app.route('/welcome')
@app.route('/')
def welcome():
    return render_template("welcome.html", cows=cows)

@app.route('/details/<cow_name>')
def details(cow_name):
    cow = next((cow for cow in cows if cow["name"] == cow_name), None)
    if cow is None:
        abort(404, description="No cow was Found with the given ID")
    return render_template("details.html", cow_name=cow_name, cow=cow)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('welcome'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('welcome'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 8085, debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)
    # Use $ export FLASK_DEBUG=1   for not rerunning it again and again.
    # flask run --port 8085     to run in debug mode.
