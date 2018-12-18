from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import PostForm
from app.models import Socialnet, Me, Post

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    view = '0'

    cats = Post.query.distinct(Post.category)
    posts = Post.query.order_by(Post.category).all()
    socialnets = Socialnet.query.all()

    me = Me.query.get(1)

    # Set mode to view by default
    mode = view

    # user wants to edit
    if request.method == 'POST':

        # get the mode value
        mode = request.form['mode']

    return render_template('index.html',
                           title='Home',
                           posts=posts,
                           mode=mode,
                           cats=cats,
                           socialnets=socialnets,
                           me=me)

# TODO Change to addPosition on next makeup
@app.route('/postform', methods=['GET','POST'])
def postform():
    form = PostForm()
    mode = '3'
    if form.validate_on_submit():
        post = post(  category=form.category.data,
                    title=form.title.data,
                    subtitle=form.subtitle.data,
                    location=form.location.data,
                    period=form.period.data,
                    description=form.description.data,
                    url=form.url.data)
        db.session.add(post)
        db.session.commit()
        flash('Please fill all the fields =)')
        return redirect(url_for('index'))
    return render_template('postform.html', title='+', form=form, mode=mode)


@app.route("/update", methods=['POST'])
def updateitem():
    # Get post id from index.html
    post_id = request.form['id']

    # Query the DB with the position id to update
    post = Post.query.filter_by(id=post_id).first()

    mode = request.form['mode']

    if request.form['action'] == 'update':

        # load updated data from index.html form
        newcategory = request.form['newcategory']
        newtitle = request.form['newtitle']
        newsubtitle = request.form['newsubtitle']
        newlocation = request.form['newlocation']
        newperiod = request.form['newperiod']
        newurl = request.form['newurl']
        newdescription = request.form['newdescription']

        # Update row with the new data
        Post.category = newcategory
        Post.title = newtitle
        Post.subtitle = newsubtitle
        Post.location = newlocation
        Post.period = newperiod
        Post.url = newurl
        Post.description = newdescription

        db.session.commit()

    if request.form['action'] == 'delete':
        # Delete the position row
        db.session.delete(post)
        db.session.commit()

    return redirect(url_for('index',mode=mode))


@app.route("/socialupdate", methods=['POST'])
def socialupdate():
    # Get post id from index.html
    socialnet_id = request.form['id']

    # Query the DB with the position id to update
    socialnet = Socialnet.query.filter_by(id=socialnet_id).first()

    mode = request.form['mode']

    if request.form['action'] == 'update':
        # Update row with the new data
        socialnet.name = request.form['newname']
        socialnet.username = request.form['newusername']
        socialnet.url = request.form['newurl']
        db.session.commit()

    if request.form['action'] == 'delete':
        # Delete the position row
        db.session.delete(socialnet)
        db.session.commit()

    return redirect(url_for('index',mode=mode))

@app.route('/socialadd', methods=['POST'])
def socialadd():
    mode = request.form['mode']

    if request.form['action'] == 'update':

        newname = request.form['newname']
        newusrname = request.form['newusrname']
        newurl = request.form['newurl']

        newnetwork = Socialnet(name=newname,username=newusrname,url=newurl)

        db.session.add(newnetwork)
        db.session.commit()

    return redirect(url_for('index',mode=mode))

@app.route("/updateme", methods=['POST'])
def updateme():
    # Get post id from index.html
    me_id = 1

    # Query the DB with the position id to update
    me = Me.query.get(1)

    mode = request.form['mode']

    if request.form['action'] == 'update':

        # load updated data from index.html form

        me.name = request.form['newname']
        me.email = request.form['newemail']
        me.phone = request.form['newphone']

        db.session.commit()


    if request.form['action'] == 'delete':
        # Delete the position row
        db.session.delete(post)
        db.session.commit()

    return redirect(url_for('index',mode=mode))
