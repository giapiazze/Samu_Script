import getopt
import sys
import datetime
import xlrd

# DB SQLAlchemy
from import_db import Session, Base
from import_models import AuthHousesUsers


# Main module to read start option parameter
# Option parameter: -d 'YYYY-mm-dd' => The date to search)
# Option parameter: -x True => If you want export)
if "__main__" == __name__:
    # Default params options
    date = datetime.datetime.now()
    s = Session()

    workbook = xlrd.open_workbook('per_importazione.xlsx')
    # AuthHousesUsers first
    worksheet = workbook.sheet_by_index(2)
    for r in range(1, 394):
        row = worksheet.row(r)

        houseId = int(row[1].value)
        userId = int(row[2].value)
        isActive = bool(row[3].value)
        startDate = date

        print(r, houseId)
        housesUsers = AuthHousesUsers(None, houseId, userId, isActive, startDate, None)

        s.add(housesUsers)

    s.commit()

    sys.exit(1)
