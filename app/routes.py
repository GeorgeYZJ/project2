from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/index')
def index():
    
    user = {'username': 'Godfrey Nyirenda'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/Quiz', methods=['GET', 'POST'])
def Quiz():
    #return redirect('/Quiz')
    return render_template('Quiz.html', title='Quiz')
    