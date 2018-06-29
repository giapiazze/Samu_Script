import os
import configparser

# DB SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuration file
config = configparser.ConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Import_CSV', 'config', 'db_config.cfg'))

# Configuration DB
pool_size = config.getint('DATABASE', 'pool_size')
db_name = config.get('DATABASE', 'db_name')
db_user = config.get('DATABASE', 'db_user')
db_pass = config.get('DATABASE', 'db_pass')
db_host = config.get('DATABASE', 'db_host')
db_port = config.getint('DATABASE', 'db_port')
db_max_overflow = config.getint('DATABASE', 'max_overflow')
db_pool_size = config.getint('DATABASE', 'pool_size')
db_echo = config.getboolean('DATABASE', 'echo')
db_recycle = config.getint('DATABASE', 'recycle')

# The DB initialization and the Session to use SQLAlchemy in Main and in single Thread.
db_uri = "mysql+mysqldb://{user}:{password}@{host}:{port}/{db}"
engine = create_engine(db_uri.format(user=db_user, password=db_pass, host=db_host,
                                     port=db_port, db=db_name),
                       echo=db_echo, pool_recycle=db_recycle)

Session = sessionmaker(
    autoflush=True,
    autocommit=False,
    bind=engine
)

Base = declarative_base()
