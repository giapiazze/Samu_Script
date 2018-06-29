from sqlalchemy import Column, String, Boolean, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from import_db import Base


class CntrMunicipality(Base):
    __tablename__ = 'cntrMunicipalities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    otherName = Column(String(128))
    municipalityProg = Column(Integer)
    cadCode = Column(String(8))
    provCapital = Column(Boolean)
    pop2011 = Column(Integer)
    metroId = Column(Integer)
    provinceId = Column(Integer)
    regionId = Column(Integer)
    geoRepartitionId = Column(Integer)
    createdAt = Column(Date)
    updatedAt = Column(Date)
    deletedAt = Column(Date)

    def __init__(self, id, name, otherName, municipalityProg, cadCode, provCapital, pop2011, metroId, provinceId,
                 regionId, geoRepartitionId, createdAt, updatedAt, deletedAt):
        self.id = id
        self.name = name
        self.otherName = otherName
        self.municipalityProg = municipalityProg
        self.cadCode = cadCode
        self.provCapital = provCapital
        self.pop2011 = pop2011
        self.metroId = metroId
        self.provinceId = provinceId
        self.regionId = regionId
        self.geoRepartitionId = geoRepartitionId
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.deletedAt = deletedAt


class EntyHouse(Base):
    __tablename__ = 'entyHouses'

    id = Column(Integer, primary_key=True)
    code = Column(String(9))
    displayName = Column(String(128))
    name = Column(String(255))
    vatCode = Column(String(16))
    cf = Column(String(16))
    email = Column(String(255))
    isActive = Column(Boolean)
    street = Column(String(255))
    provinceId = Column(Integer)
    municipalityId = Column(Integer)
    zip = Column(String(8))
    locality = Column(String(64))
    x = Column(Float)
    y = Column(Float)
    h = Column(Integer)
    houseId = Column(Integer)
    categoryId = Column(Integer)
    kindId = Column(Integer)
    createdAt = Column(Date)
    updatedAt = Column(Date)
    deletedAt = Column(Date)

    def __init__(self, id, code, displayName, name, vatCode, cf, email, isActive, street,
                 provinceId, municipalityId, zip, locality, x, y, h, houseId, categoryId, kindId,
                 createdAt, updatedAt, deletedAt):
        self.id = id
        self.code = code
        self.displayName = displayName
        self.name = name
        self.vatCode = vatCode
        self.cf = cf
        self.email = email
        self.isActive = isActive
        self.street = street
        self.provinceId = provinceId
        self.municipalityId = municipalityId
        self.zip = zip
        self.locality = locality
        self.x = x
        self.y = y
        self.h = h
        self.houseId = houseId
        self.categoryId = categoryId
        self.kindId = kindId
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.deletedAt = deletedAt


class MeasMeter(Base):
    __tablename__ = 'measMeters'

    id = Column(Integer, primary_key=True)
    regNumber = Column(String(64))
    x = Column(Float)
    y = Column(Float)
    unit = Column(String(8))
    sortId = Column(Integer)
    supplierId = Column(Integer)
    utilizationId = Column(Integer)
    meterId = Column(Integer)
    createdAt = Column(Date)
    updatedAt = Column(Date)
    deletedAt = Column(Date)

    def __init__(self, id, regNumber, x, y, unit, sortId, supplierId, utilizationId, meterId,
                 createdAt, updatedAt, deletedAt):
        self.id = id
        self.regNumber = regNumber
        self.x = x
        self.y = y
        self.unit = unit
        self.sortId = sortId
        self.supplierId = supplierId
        self.utilizationId = utilizationId
        self.meterId = meterId
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.deletedAt = deletedAt


class MeasHousesMeters(Base):
    __tablename__ = 'measHousesMeters'

    id = Column(Integer, primary_key=True)
    houseId = Column(Integer)
    isActive = Column(Boolean)
    startDate = Column(Date)
    endDate = Column(Date)

    meterId = Column(Integer, ForeignKey('measMeters.id'))

    meter = relationship("MeasMeter", back_populates = "housesMeters")

    def __init__(self, id, houseId, meterId, isActive, startDate, endDate):
        self.id = id
        self.houseId = houseId
        self.meterId = meterId
        self.isActive = isActive
        self.startDate = startDate
        self.endDate = endDate


MeasMeter.housesMeters = relationship("MeasHousesMeters", order_by = MeasHousesMeters.id, back_populates = "meter")


class AuthHousesUsers(Base):
    __tablename__ = 'authHousesUsers'

    id = Column(Integer, primary_key=True)
    houseId = Column(Integer)
    userId = Column(Integer)
    isActive = Column(Boolean)
    startDate = Column(Date)
    endDate = Column(Date)

    def __init__(self, id, houseId, userId, isActive, startDate, endDate):
        self.id = id
        self.houseId = houseId
        self.userId = userId
        self.isActive = isActive
        self.startDate = startDate
        self.endDate = endDate