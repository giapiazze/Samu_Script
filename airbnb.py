import getopt
import sys
import datetime

# DB SQLAlchemy
from airbnb_db import Session, Base
from airbnb_models import House, Price
from airbnb_analysis import http_analysis


# Main module to read start option parameter
# Option parameter: -d 'YYYY-mm-dd' => The date to search)
# Option parameter: -x True => If you want export)
if "__main__" == __name__:
    # Default params options
    export = False
    date = datetime.datetime.now().strftime('%Y-%m-%d')

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:x:", ["directory", "grammar="])
    except getopt.GetoptError as err:
        print("Params Errors: ", err)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            sys.exit()
        elif opt in ("-d", "--date"):
            if arg != '' or arg is not None:
                try:
                    date = datetime.datetime.strptime(arg, '%Y-%m-%d').strftime('%Y-%m-%d')
                except ValueError:
                    raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        elif opt in ("-x", "--export"):
            if arg != 0 or arg == 1:
                export = True

    s = Session()
    houses = s.query(House).all()
    for h in houses:
        http_analysis(h, date)
    print(houses)

    sys.exit(1)
