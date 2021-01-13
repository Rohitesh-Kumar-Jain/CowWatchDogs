from flask import render_template, abort, url_for, flash, redirect
from CWD import app,db, bcrypt
from CWD.forms import RegistrationForm, LoginForm
from CWD.models import User,Cow

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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
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