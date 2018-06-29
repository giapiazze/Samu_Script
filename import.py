import getopt
import sys
import datetime
import xlrd

# DB SQLAlchemy
from import_db import Session, Base
from import_models import EntyHouse, CntrMunicipality, MeasMeter, MeasHousesMeters
from import_exec import http_analysis


# Main module to read start option parameter
# Option parameter: -d 'YYYY-mm-dd' => The date to search)
# Option parameter: -x True => If you want export)
if "__main__" == __name__:
    # Default params options
    date = datetime.datetime.now()
    s = Session()

    workbook = xlrd.open_workbook('anagrafica_alleanza.xlsx')
    # EntyHouses first
    worksheet = workbook.sheet_by_index(0)
    for r in range(1, 783):
        row = worksheet.row(r)
        id = int(row[0].value)
        print(r, id)
        if id >= 325:
            code = row[2].value
            displayName = row[3].value
            name = row[1].value
            vatCode = None
            cf = None
            email = None
            isActive = True
            street = row[4].value
            provinceId = None
            municipalityId = None
            for instance in s.query(CntrMunicipality).filter(CntrMunicipality.name == row[6].value):
                provinceId = instance.provinceId
                municipalityId = instance.id
            zip = str(int(row[7].value))
            locality = None
            x = float(row[8].value)
            y = float(row[9].value)
            h = int(row[10].value)

            tmp = row[12].value
            if tmp == '':
                houseId = None
            else:
                houseId = int(row[12].value)

            tmp = row[11].value
            if tmp == '':
                categoryId = None
            else:
                categoryId = int(row[11].value)

            tmp = row[13].value
            if tmp == '':
                kindId = None
            else:
                kindId = int(row[13].value)

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
    for r in range(1, 854):
        row = worksheet.row(r)
        isActive = True
        startDate = datetime.datetime(2017, 1, 1, 12, 0, 0, 0)
        endDate = None
        houseId = int(row[6].value)
        housesMeters = MeasHousesMeters(None, houseId, None, isActive, startDate, endDate)

        id = int(row[0].value)
        regNumber = row[1].value
        x = None
        y = None
        unit = row[2].value
        sortId = int(row[3].value)
        tmp = row[4].value
        if tmp == '':
            supplierId = None
        else:
            supplierId = int(row[4].value)

        tmp = row[5].value
        if tmp == '':
            utilizationId = None
        else:
            utilizationId = int(row[5].value)
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
