from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('idNumber', Integer, primary_key=True, nullable=False),
    Column('firstName', String(length=120)),
    Column('lastName', String(length=120)),
    Column('email', String(length=120)),
    Column('interestGrad', String(length=120)),
    Column('interestSchool', String(length=120)),
    Column('major', String(length=120)),
    Column('otherMajor', String(length=120)),
    Column('degree', String(length=120)),
    Column('doneDate', String(length=120)),
    Column('major2', String(length=120)),
    Column('otherMajor2', String(length=120)),
    Column('degree2', String(length=120)),
    Column('doneDate2', String(length=120)),
    Column('areasInterest', String(length=120)),
    Column('additionalInfo', String(length=120)),
    Column('file', LargeBinary),
    Column('fileName', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['file'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['file'].drop()
