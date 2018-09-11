from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import JobPostForm
from app.models import Job, Social, Me

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    view = '0'

    cats = Job.query.distinct(Job.category)

    jobs = Job.query.order_by(Job.category).all()

    # Set mode to view by default
    mode = view

    # user wants to edit
    if request.method == 'POST':

        # get the mode value
        mode = request.form['mode']

    return render_template('index.html',
                           title='Home',
                           jobs=jobs,
                           mode=mode,
                           cats=cats)

# TODO Change to addPosition on next makeup
@app.route('/jobform', methods=['GET','POST'])
def jobform():
    form = JobPostForm()
    mode = '3'
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
    return render_template('jobform.html', title='+', form=form, mode=mode)


@app.route("/update", methods=['POST'])
def update():
    # Get job id from index.html
    job_id = request.form['id']

    # Query the DB with the position id to update
    job = Job.query.filter_by(id=job_id).first()

    mode = request.form['mode']

    if request.form['action'] == 'update':

        # load updated data from index.html form
        newcategory = request.form['newcategory']
        newtitle = request.form['newtitle']
        newsubtitle = request.form['newsubtitle']
        newlocation = request.form['newlocation']
        newperiod = request.form['newperiod']
        newdescription = request.form['newdescription']

        # Update row with the new data
        job.category = newcategory
        job.title = newtitle
        job.subtitle = newsubtitle
        job.location = newlocation
        job.period = newperiod
        job.description = newdescription

        db.session.commit()


    if request.form['action'] == 'delete':
        # Delete the position row
        db.session.delete(job)
        db.session.commit()



    return redirect(url_for('index',mode=mode))