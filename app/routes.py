from flask import render_template, flash, redirect, url_for,request,g
from app import app, db
from app.forms import LoginForm, RegistrationForm,PostForm, AnswerForm
from flask_login import current_user, login_user
from app.models import User, Post,Answer
from flask_login import logout_user, login_required
from werkzeug.urls import url_parse






@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    user = current_user.username
    if form.validate_on_submit():
        post = Post(question=form.question.data, body= form.post.data,  author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))
    posts = current_user.posts.all()
    return render_template('index.html', title='Home', user=user, posts=posts, form = form)

ur = current_user

@app.route('/Quiz', methods=['GET', 'POST'])
def url():
    uu = current_user.username
    return redirect(url_for("Quiz", name= uu ))

@app.route('/Quiz/<name>', methods=['GET', 'POST'])
def Quiz(name):
    posts =  Post.query.all()
    q = [post.question for post in Post.query.all()]
    user = current_user.username
    if request.method == "POST":
        ques = request.form.get("question")
        ans = request.form.get("answer")
        attemp = Answer(answer = ans, feedback=Post.query.filter(Post.question == ques).first(), attemp = current_user)
        db.session.add(attemp)
        db.session.commit()
        post = Post.query.filter(Post.question == ques).first()
        if (ques.lower() not in q and ans is not None):            
            flash ("Please enter the existing question")
        else:
            if (post.body == ans.lower()):
                flash('Your answer is correct!')
            elif(post.body != ans.lower()):
                flash("Your answer is not correct!")
            
    return render_template('Quiz.html', title='QuizPage', posts=posts, user=user)
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)