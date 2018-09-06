from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, JobPostForm
from app.models import Job

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    # Get the list of positions
    jobs = Job.query.all()

    # Set mode to view
    mode = '0'

    # user wants to edit
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

@app.route("/update", methods=['POST'])
def update():
    newcategory = request.form['newcategory']
    job_id = request.form['id']
    job = Job.query.filter_by(id=job_id).first()
    job.category = newcategory
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/delete", methods=["POST"])
def delete():
    job_id = request.form['id']
    job = Job.query.filter_by(id=job_id).first()
    db.session.delete(job)
    db.session.commit()
    return redirect("/")