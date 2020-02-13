import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

env = os.environ['HOWDY_JOB_ENV']

if env == 'local' or env == 'development':
  ECHO_LOG = True
else:
  ECHO_LOG = False

if env == 'local':
  DATABASE = 'postgresql'
  USER = os.environ['HOWDY_JOB_DB_USER']
  PASSWORD = os.environ['HOWDY_JOB_DB_PASSWORD']
  HOST = os.environ['HOWDY_JOB_DB_HOST']
  DB_NAME = os.environ['HOWDY_JOB_DB_NAME']
  CONNECT_STR = '{}://{}@{}/{}'.format(DATABASE, USER, HOST, DB_NAME)
else:
  CONNECT_STR = os.environ['DATABASE_URL']

engine = create_engine(
  CONNECT_STR, echo=ECHO_LOG,
)

Session = sessionmaker(bind=engine)
session = Session()
