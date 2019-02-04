import getopt
import sys
import datetime
import xlrd

# DB SQLAlchemy
from import_db import Session, Base
from import_models import EntyHouse, CntrMunicipality, MeasMeter, MeasHousesMeters


# Main module to read start option parameter
# Option parameter: -d 'YYYY-mm-dd' => The date to search)
# Option parameter: -x True => If you want export)
if "__main__" == __name__:
    # Default params options
    date = datetime.datetime.now()
    s = Session()

    workbook = xlrd.open_workbook('da_importare.xlsx')
    # EntyHouses first
    worksheet = workbook.sheet_by_index(0)
    for r in range(1, worksheet.nrows):
        row = worksheet.row(r)
        id = int(row[0].value)
        print(r, id)
        if id >= 325:
            code = row[1].value
            displayName = row[2].value
            name = row[3].value
            vatCode = None
            cf = None
            email = None
            isActive = True
            street = row[8].value
            provinceId = row[9].value
            municipalityId = row[10].value
            zip = row[11].value
            locality = None
            x = float(row[13].value)
            y = float(row[14].value)
            h = int(row[15].value)

            tmp = row[16].value
            if tmp == '' or tmp == 'NULL':
                houseId = None
            else:
                houseId = int(tmp)

            tmp = row[17].value
            if tmp == '' or tmp == 'NULL':
                categoryId = None
            else:
                categoryId = int(tmp)

            tmp = row[18].value
            if tmp == '' or tmp == 'NULL':
                kindId = None
            else:
                kindId = int(tmp)

            date = datetime.datetime.now()
            createdAt = date
            updatedAt = date
            deletedAt = None

            print(r, name)
            house = EntyHouse(id, code, displayName, name, vatCode, cf, email, isActive, street, provinceId,
                              municipalityId, zip, locality, x, y, h, houseId, categoryId, kindId,
                              createdAt, updatedAt, deletedAt)

            s.add(house)

    worksheet = workbook.sheet_by_index(1)
    for r in range(1, worksheet.nrows):
        row = worksheet.row(r)
        isActive = True
        startDate = datetime.datetime(2017, 1, 1, 12, 0, 0, 0)
        endDate = None
        houseId = int(row[12].value)
        housesMeters = MeasHousesMeters(None, houseId, None, isActive, startDate, endDate)

        id = int(row[0].value)
        regNumber = str(row[1].value)
        x = None
        y = None
        unit = row[4].value
        sortId = int(row[5].value)
        tmp = row[6].value
        if tmp == '' or tmp == 'NULL':
            supplierId = None
        else:
            supplierId = int(row[6].value)

        tmp = row[7].value
        if tmp == '' or tmp == 'NULL':
            utilizationId = None
        else:
            utilizationId = int(row[7].value)
        date = datetime.datetime.now()
        createdAt = date
        updatedAt = date
        deletedAt = None

        print(r, id, regNumber)
        meter = MeasMeter(id, regNumber, x, y, unit, sortId, supplierId, utilizationId, None, createdAt,
                          updatedAt, deletedAt)
        housesMeters.meter = meter

        s.add(housesMeters)

    s.commit()

    sys.exit(1)
