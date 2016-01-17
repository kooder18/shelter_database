import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):

    __tablename__ = 'shelter'

    name = Column(
    String(80), nullable = False)

    address = Column(
    String(250))

    city = Column(
    String(80))

    state = Column(
    String(30))

    zipCode = Column(
    Integer
    )

    website = Column(
    String(120)
    )
    id = Column(
    Integer, primary_key = True)




class Puppy(Base):

    __tablename__ = 'puppy'

    name = Column(String(80), nullable =
    False)
    dob = Column(String(20))
    gender = Column(String(20))
    weight = Column(Integer)
    shelter_id = Column(
    Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)





#####################insert at end of file ###############3

engine = create_engine(
'sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
