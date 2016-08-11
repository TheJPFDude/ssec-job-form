from flask_wtf import Form
from wtforms import StringField, SelectField, RadioField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField

# Form for entering/editing data into database
class EntryForm(Form):
    firstName = StringField('firstName', validators=[DataRequired()])
    lastName = StringField('lastName', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    interestGrad = RadioField('interestGrad', coerce=str, choices=[('Yes', 'Yes'), ('No', 'No')],
                              validators=[DataRequired()])
    interestSchool = RadioField('interestSchool', coerce=str, choices=[('Yes', 'Yes'), ('No', 'No')],
                                validators=[DataRequired()])
    major = SelectField('major', coerce=str,
                        choices=[('N/A', 'N/A'), ('CS', 'Computer Science'),
                                ('CE', 'Computer Engineering'), ('EE', 'Electrical Engineering'),
                                ('Math', 'Mathematics'), ('Physics', 'Physics'),
                                ('Other', 'Other (enter specific major below)')])
    otherMajor = StringField('otherMajor')

    degree = RadioField('degree', coerce=str,
                        choices=[('None', 'N/A'), ('Bachelor\'s', 'Bachelor\'s'), ('Master\'s', 'Master\'s'), ('PhD', 'PhD')])
    doneDate = SelectField('doneDate', coerce=str,
                           choices=[('None', 'N/A'), ('Graduated', 'Already Graduated'), ('Fall 2016', 'Fall 2016'),
                                    ('Spring 2017', 'Spring 2017'), ('Summer 2017', 'Summer 2017'), ('Fall 2017', 'Fall 2017'),
                                    ('Spring 2018', 'Spring 2018'), ('Summer 2018', 'Summer 2018'), ('Fall 2018', 'Fall 2018'),
                                    ('Spring 2019', 'Spring 2019'), ('Summer 2019', 'Summer 2019'), ('Fall 2019', 'Fall 2019'),
                                    ('Spring 2020', 'Spring 2020'), ('Summer 2020', 'Summer 2020'), ('Fall 2020', 'Fall 2020')])
    major2 = SelectField('major2', coerce=str,
                         choices=[('N/A', 'N/A'), ('CS', 'Computer Science'),
                                 ('CE', 'Computer Engineering'), ('EE', 'Electrical Engineering'),
                                 ('Math', 'Mathematics'), ('Physics', 'Physics'),
                                 ('Other', 'Other (enter specific major below)')])
    otherMajor2 = StringField('otherMajor2')
    degree2 = RadioField('degree2', coerce=str,
                         choices=[('None', 'N/A'), ('Bachelor\'s', 'Bachelor\'s'), ('Master\'s', 'Master\'s'), ('PhD', 'PhD')])
    doneDate2 = SelectField('doneDate2', coerce=str,
                            choices=[('N/A', 'N/A'), ('Graduated', 'Already Graduated'), ('Fall 2016', 'Fall 2016'),
                                     ('Spring 2017', 'Spring 2017'), ('Summer 2017', 'Summer 2017'), ('Fall 2017', 'Fall 2017'),
                                     ('Spring 2018', 'Spring 2018'), ('Summer 2018', 'Summer 2018'), ('Fall 2018', 'Fall 2018'),
                                     ('Spring 2019', 'Spring 2019'), ('Summer 2019', 'Summer 2019'), ('Fall 2019', 'Fall 2019'),
                                     ('Spring 2020', 'Spring 2020'), ('Summer 2020', 'Summer 2020'), ('Fall 2020', 'Fall 2020')])
    areasInterest = StringField('areasInterest')
    additionalInfo = StringField('additionalInfo')
    file = FileField('file')
    fileName = StringField('fileName')


# Form for deleting data from database
class DeleteForm(Form):
    idNumber = StringField('idNumber', validators=[DataRequired()])