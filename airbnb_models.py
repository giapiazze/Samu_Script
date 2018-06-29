from sqlalchemy import Column, String, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from airbnb_db import Base


class House(Base):
    __tablename__ = 'houses'

    id = Column(Integer, primary_key=True)
    airbnb_id = Column(String(16), unique=True)
    description = Column(String)
    location = Column(String(64))
    adults = Column(Integer)
    s = Column(String(16))
    prices = relationship("Price", back_populates="house")

    def __init__(self, airbnb_id, description, location, adults, s):
        self.airbnb_id = airbnb_id
        self.description = description
        self.location = location
        self.adults = adults
        self.s = s


class Price(Base):
    __tablename__ = 'prices'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    from_date = Column(Date)
    to_date = Column(Date)
    price = Column(Float)
    house_id = Column(Integer, ForeignKey('houses.id'))
    house = relationship("House", back_populates="prices")

    def __init__(self, date, from_date, to_date, price):
        self.date = date
        self.from_date = from_date
        self.to_date = to_date
        self.price = price
