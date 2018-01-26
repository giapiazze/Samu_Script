import getopt
import sys
import time
import datetime
import ConfigParser
import traceback

# DB SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table, func, not_
from sqlalchemy.orm import sessionmaker, mapper

# Configuration file
config = ConfigParser.ConfigParser()
config.read('Airbnb/db_config.cfg')

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
db_uri = "mysql://{user}:{password}@{host}:{port}/{db}"
db_engine = create_engine(db_uri.format(user=db_user, password=db_pass, host=db_host,
                                        port=db_port, db=db_name),
                          echo=db_echo, pool_recycle=db_recycle)
DBSession = sessionmaker(
    autoflush=True,
    autocommit=False,
    bind=db_engine
)
metadata = MetaData(db_engine)


# These are the empty classes that will become our data classes
# and the relatives auto-import from DB table
class House(object):
    pass


class Offer(object):
    pass


houses = Table('Houses', metadata, autoload=True)
offers = Table('Offers', metadata, autoload=True)

# Table Mapper
house_mapper = mapper(House, houses)
offer_mapper = mapper(Offer, offers)


# Main module to read start option parameter
# Option parameter: -d 'C:/Documents/' => The folder to search in)
if "__main__" == __name__:
    # Default params options
    recur = True

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:r:", ["directory", "grammar="])
    except getopt.GetoptError as err:
        print("Params Errors ;", err)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            sys.exit()
        elif opt in ("-d", "--directory"):
            if arg != 0 or arg is not None:
                path = arg
        elif opt in ("-r", "--recursive"):
            if arg != 1 or arg == 0:
                recur = False

    array_result = run()