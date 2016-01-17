from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppies import Base, Shelter, Puppy

engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)

session = DBSession()

#items = session.query(Shelter).all()
#for item in items:
#    print item.name

'''
Function returns a query where the puppy names
are in ascending alpabetical order

'''
def ascend_alphabet():
    puppies = session.query(Puppy).order_by(Puppy.name.desc())
    for puppy in puppies:
        print puppy.name


'''
Function returns a query for puppies where the
puppy names are in descending alpabetical order
'''
def descend_alphabet():
    puppies = session.query(Puppy).order_by(Puppy.name)
    for puppy in puppies:
        print puppy.name



ascend_alphabet()
