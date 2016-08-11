from flask import Flask, render_template, flash, redirect, request, Response, url_for, send_file, make_response, send_from_directory, current_app
from app import app, db, models
from .forms import EntryForm, DeleteForm
from functools import wraps
from werkzeug.utils import secure_filename
import sqlalchemy, os, docx2txt

engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=False)
Session = sqlalchemy.orm.scoped_session( sqlalchemy.orm.sessionmaker( bind = engine ) )
sess = Session()

counter = 0
fileName = ''

# Method to set username and password
def check_auth(username, password):
    return username == 'ssec' and password == 'ssec'

# Method to authenticate username and password
def authenticate():
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

# Helper that requires username/password for access
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

UPLOAD_FOLDER = 'files'
ALLOWED_EXTENSIONS = set(['docx', 'txt', 'pdf'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# The home screen of the site where data is entered
@app.route('/', methods=['GET', 'POST'])
def index():
    global fileName
    global counter
    boolToTrack = True

    user = models.User()
    form = EntryForm(request.form, obj=user)
    # Preventing the data in otherMajor to be submitted if "Other" not chosen as major
    if form.major.data != "Other":
        form.otherMajor.data = form.major.data

    if form.major2.data != "Other":
        form.otherMajor2.data = form.major2.data

    if request.method == 'POST' and 'file' in request.files:
        file = request.files['file']

        form.file = file

        if file and allowed_file(file.filename):

            # Renaming file if it is same name as a file in the uploaded files folder
            if os.path.isfile(UPLOAD_FOLDER + '/' + file.filename):
                for n in range(1, 51):
                    numFile = (str(n) + ".").join(file.filename.rsplit('.', 1))
                    print(numFile)
                    if os.path.isfile(UPLOAD_FOLDER + '/' + numFile):
                        file.filename = (str(n + 1) + ".").join(file.filename.rsplit('.', 1))
                        boolToTrack = False
                        break
                if boolToTrack:
                    file.filename = ("1.").join(file.filename.rsplit('.', 1))

            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fileName = filename
            counter = 0
        elif not allowed_file(file.filename) and not file.filename == '':
            counter = 1

    form.fileName.data = fileName
    user.file = form.file

    if form.validate_on_submit():
        if counter == 0:
            # Adding the data to the database and committing it
            form.populate_obj(user)
            db.session.add(user)
            db.session.commit()
            flash('Entry Submitted')
            # Returning to the data entry screen
            return redirect('/')
        elif counter == 1:
            flash('File Type Not Accepted')
            return redirect('/')
    try:
        return render_template('index.html',
                                title='Enter Info Here',
                                form=form)
    except AttributeError as e:
        flash('Please fill in the required fields')
        sess.rollback()
        return redirect('/')

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload/<path:fileName>', methods=['GET', 'POST'])
def upload(fileName):
    uploads = os.path.join(app.config['UPLOAD_FOLDER'], fileName)
    content = ''
    headers = {"Content-Disposition": "attachment; filename=%s" % fileName}
    if fileName[-4:] == '.txt' or fileName[-4:] == '.pdf':
        file = open(uploads, 'r+')
        content = file.read()
        file.close()
    elif fileName[-5:] == '.docx':
        content = docx2txt.process(uploads)
    return make_response((content, headers))

# Retrieving the data from the database and displaying it onto the screen
@app.route('/data')
@requires_auth
def data():
    db.create_all()
    users = models.User.query.all()
    return render_template('data.html',
                           title='Database Data',
                           form=users)

# Editing entries from the database
@app.route('/edit/<int:idNumber>', methods=['GET', 'POST'])
@requires_auth
def edit(idNumber):
    global fileName
    global counter
    boolToTrack = True

    user_id = idNumber
    user = models.User.query.get(user_id)
    form = EntryForm(request.form, obj=user)

    # Preventing the data in otherMajor to be submitted if "Other" not chosen as major
    if form.major.data != "Other":
        form.otherMajor.data = form.major.data

    if form.major2.data != "Other":
        form.otherMajor2.data = form.major2.data

    if request.method == 'POST' and 'file' in request.files:
        file = request.files['file']

        form.file = file

        if file and allowed_file(file.filename):

            # Renaming file if it is same name as a file in the uploaded files folder
            if os.path.isfile(UPLOAD_FOLDER + '/' + file.filename):
                for n in range(1, 51):
                    numFile = (str(n) + ".").join(file.filename.rsplit('.', 1))
                    print(numFile)
                    if os.path.isfile(UPLOAD_FOLDER + '/' + numFile):
                        file.filename = (str(n + 1) + ".").join(file.filename.rsplit('.', 1))
                        boolToTrack = False
                        break
                if boolToTrack:
                    file.filename = ("1.").join(file.filename.rsplit('.', 1))

            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fileName = filename
            counter = 0
        elif not allowed_file(file.filename) and not file.filename == '':
            counter = 1

    form.fileName.data = fileName
    user.file = form.file

    if form.validate_on_submit():
        if counter == 0:
            # Adding the data to the database and committing it
            form.populate_obj(user)
            db.session.commit()
            flash('Entry Edited')
            # Returning to the database screen
            return redirect('/edit/' + str(idNumber))
        elif counter == 1:
            flash('File Type Not Accepted')
            return redirect('/edit/' + str(idNumber))
    try:
        return render_template('edit.html',
                            title='Edit Data',
                            form=form)
    except AttributeError as e:
        flash('Please fill in the required fields')
        sess.rollback()
        return redirect('/edit/' + str(idNumber))

# Deleting entries from the database
@app.route('/delete', methods=['GET', 'POST'])
@requires_auth
def delete():
    form = DeleteForm()
    if form.validate_on_submit():
        # Assigning entered data to the model object
        toDelete = models.toDelete()
        toDelete.idNumber = form.idNumber
        form.populate_obj(toDelete)

        # Getting the "entry to delete" from the database
        userToDelete = models.User.query.get(toDelete.idNumber)

        try:
            # Deleting entry from the database and committing changes
            db.session.delete(userToDelete)
            db.session.commit()
            # Reassigning ID numbers
            users = models.User.query.all()
            i = 1
            for user in users:
                user.idNumber = i
                i += 1

            db.session.commit()
            flash('Entry Deleted')
            # Returning to the database screen
            return redirect('/delete')

        # Happens when error in typing ID: flashes message and redirects to deletion screen
        except sqlalchemy.exc.SQLAlchemyError as e:
            flash('Please enter a valid ID')
            sess.rollback()
            return redirect('/delete')

    return render_template('delete.html',
                           title='Delete Data',
                           form=form)

# Sorting the entries in the database by alphabetical order
@app.route('/data/<variable>', methods=['GET', 'POST'])
def sort(variable):
    users = models.User.query.order_by(variable)

    return render_template('data.html',
                           title='Sort Data',
                           form=users)