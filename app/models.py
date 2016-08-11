from app import db

# Class for entries from database
class User(db.Model):
    idNumber = db.Column(db.Integer, primary_key = True, autoincrement=True)
    firstName = db.Column(db.String(120), index=True)
    lastName = db.Column(db.String(120), index=True)
    email = db.Column(db.String(120), index=True)
    interestGrad = db.Column(db.String(120), index=True)
    interestSchool = db.Column(db.String(120), index=True)
    major = db.Column(db.String(120), index=True)
    otherMajor = db.Column(db.String(120), index=True)
    degree = db.Column(db.String(120), index=True)
    doneDate = db.Column(db.String(120), index=True)
    major2 = db.Column(db.String(120), index=True)
    otherMajor2 = db.Column(db.String(120), index=True)
    degree2 = db.Column(db.String(120), index=True)
    doneDate2 = db.Column(db.String(120), index=True)
    areasInterest = db.Column(db.String(120), index=True)
    additionalInfo = db.Column(db.String(120), index=True)
    fileName = db.Column(db.String(120), index=True)

    def __repr__(self):
        return '<User %r>' % self.idNumber

# Class for deleting entries in database
class toDelete(db.Model):
    idNumber = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<toDelete %r>' % self.idNumber