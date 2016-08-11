from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
submitted = Table('submitted', pre_meta,
    Column('idNumber', INTEGER, primary_key=True, nullable=False),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('firstName', VARCHAR(length=120)),
    Column('lastName', VARCHAR(length=120)),
    Column('email', VARCHAR(length=120)),
    Column('major', VARCHAR(length=120)),
    Column('areasInterest', VARCHAR(length=120)),
    Column('description', VARCHAR(length=120)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('firstName', String(length=120)),
    Column('lastName', String(length=120)),
    Column('email', String(length=120)),
    Column('major', String(length=120)),
    Column('otherMajor', String(length=120)),
    Column('degree', String(length=120)),
    Column('doneDate', String(length=120)),
    Column('major2', String(length=120)),
    Column('otherMajor2', String(length=120)),
    Column('degree2', String(length=120)),
    Column('doneDate2', String(length=120)),
    Column('interestGrad', String(length=120)),
    Column('interestSchool', String(length=120)),
    Column('areasInterest', String(length=120)),
    Column('additionalInfo', String(length=120)),
)

to_edit = Table('to_edit', pre_meta,
    Column('idNumber', INTEGER, primary_key=True, nullable=False),
    Column('firstName', VARCHAR(length=120)),
    Column('lastName', VARCHAR(length=120)),
    Column('email', VARCHAR(length=120)),
    Column('major', VARCHAR(length=120)),
    Column('areasInterest', VARCHAR(length=120)),
    Column('description', VARCHAR(length=120)),
)

to_edit = Table('to_edit', post_meta,
    Column('idNumber', Integer, primary_key=True, nullable=False),
    Column('firstName', String(length=120)),
    Column('lastName', String(length=120)),
    Column('email', String(length=120)),
    Column('major', String(length=120)),
    Column('otherMajor', String(length=120)),
    Column('degree', String(length=120)),
    Column('doneDate', String(length=120)),
    Column('major2', String(length=120)),
    Column('otherMajor2', String(length=120)),
    Column('degree2', String(length=120)),
    Column('doneDate2', String(length=120)),
    Column('interestGrad', String(length=120)),
    Column('interestSchool', String(length=120)),
    Column('areasInterest', String(length=120)),
    Column('additionalInfo', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['submitted'].drop()
    pre_meta.tables['user'].columns['description'].drop()
    post_meta.tables['user'].columns['additionalInfo'].create()
    post_meta.tables['user'].columns['degree'].create()
    post_meta.tables['user'].columns['degree2'].create()
    post_meta.tables['user'].columns['doneDate'].create()
    post_meta.tables['user'].columns['doneDate2'].create()
    post_meta.tables['user'].columns['interestGrad'].create()
    post_meta.tables['user'].columns['interestSchool'].create()
    post_meta.tables['user'].columns['major2'].create()
    post_meta.tables['user'].columns['otherMajor'].create()
    post_meta.tables['user'].columns['otherMajor2'].create()
    pre_meta.tables['to_edit'].columns['description'].drop()
    post_meta.tables['to_edit'].columns['additionalInfo'].create()
    post_meta.tables['to_edit'].columns['degree'].create()
    post_meta.tables['to_edit'].columns['degree2'].create()
    post_meta.tables['to_edit'].columns['doneDate'].create()
    post_meta.tables['to_edit'].columns['doneDate2'].create()
    post_meta.tables['to_edit'].columns['interestGrad'].create()
    post_meta.tables['to_edit'].columns['interestSchool'].create()
    post_meta.tables['to_edit'].columns['major2'].create()
    post_meta.tables['to_edit'].columns['otherMajor'].create()
    post_meta.tables['to_edit'].columns['otherMajor2'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['submitted'].create()
    pre_meta.tables['user'].columns['description'].create()
    post_meta.tables['user'].columns['additionalInfo'].drop()
    post_meta.tables['user'].columns['degree'].drop()
    post_meta.tables['user'].columns['degree2'].drop()
    post_meta.tables['user'].columns['doneDate'].drop()
    post_meta.tables['user'].columns['doneDate2'].drop()
    post_meta.tables['user'].columns['interestGrad'].drop()
    post_meta.tables['user'].columns['interestSchool'].drop()
    post_meta.tables['user'].columns['major2'].drop()
    post_meta.tables['user'].columns['otherMajor'].drop()
    post_meta.tables['user'].columns['otherMajor2'].drop()
    pre_meta.tables['to_edit'].columns['description'].create()
    post_meta.tables['to_edit'].columns['additionalInfo'].drop()
    post_meta.tables['to_edit'].columns['degree'].drop()
    post_meta.tables['to_edit'].columns['degree2'].drop()
    post_meta.tables['to_edit'].columns['doneDate'].drop()
    post_meta.tables['to_edit'].columns['doneDate2'].drop()
    post_meta.tables['to_edit'].columns['interestGrad'].drop()
    post_meta.tables['to_edit'].columns['interestSchool'].drop()
    post_meta.tables['to_edit'].columns['major2'].drop()
    post_meta.tables['to_edit'].columns['otherMajor'].drop()
    post_meta.tables['to_edit'].columns['otherMajor2'].drop()
