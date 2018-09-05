from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, JobPostForm
from app.models import Job

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    #user = {'username': 'r2'}
    jobs = Job.query.all()

    mode = '0'

    if request.method == 'POST':
        mode = request.form['mode']

    return render_template('index.html',
                           title='Home',
                           jobs=jobs,
                           mode=mode)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('/index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/jobform', methods=['GET','POST'])
def jobform():
    form = JobPostForm()
    if form.validate_on_submit():
        job = Job(  category=form.category.data,
                    title=form.title.data,
                    subtitle=form.subtitle.data,
                    location=form.location.data,
                    period=form.period.data,
                    description=form.description.data)
        db.session.add(job)
        db.session.commit()
        flash('Please fill all the fields =)')
        return redirect(url_for('index'))
    return render_template('jobform.html', title='+', form=form)

@app.route('/edit',methods=['GET','POST'])
def edit():
    form = JobPostForm()
    job = Job.query.get(1)

    form.category.data = job.category
    form.title.data = job.title
    form.subtitle.data = job.subtitle
    form.location.data = job.location
    form.period.data = job.period
    form.description.data = job.description

    if request.method == 'POST':

        db.session.commit()
        flash('Updated fields')
        return redirect(url_for('index'))

    return render_template('jobform.html', title='+', form=form)
