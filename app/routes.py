from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm, JobPostForm
from app.models import Job

@app.route('/')
@app.route('/index')
def index():
    #user = {'username': 'r2'}
    jobs = Job.query.all()
    return render_template('index.html', title='Home', jobs=jobs)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('/index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/addjob', methods=['GET','POST'])
def addjob():
    form = JobPostForm()
    if form.validate_on_submit():
        job = Job(category=form.category.data, title=form.title.data)
        db.session.add(job)
        db.session.commit()
        flash('Please fill all the fields =)')
        return redirect(url_for('/addjob'))
    return render_template('addjob.html', title='+', form=form)