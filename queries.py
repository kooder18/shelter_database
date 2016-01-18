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
Returns a query for puppies where the
puppy names are in descending alpabetical order
'''
def descend_alphabet():
    puppies = session.query(Puppy).order_by(Puppy.name)
    for puppy in puppies:
        print puppy.name

'''
Returns a query of puppies that are less
than 6 months old organized by youngest first
'''
def young_pups():
    puppies = session.query(Puppy).order_by(Puppy.dateOfBirth.desc())
    for puppy in puppies:
        print puppy.dateOfBirth

'''
Returns a query of all puppies by weight
ascending
'''
def puppy_weight():
    puppies = session.query(Puppy).order_by(Puppy.weight)
    for puppy in puppies:
        print puppy.weight

'''
Returns a query of all puppies grouped by the shelter
they are staying in.function takes an arugment of the shelter_id
'''

def puppy_shelter(id):
    puppies = session.query(Puppy).filter_by(shelter_id = id)
    for puppy in puppies:
        print puppy.name
    print "All puppies in shelter ",  id
    print "\n"


puppy_shelter(2)
