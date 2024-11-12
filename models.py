from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base,relationship

db_user = "sqlite:///database.db"
engine  = create_engine(db_user)

Base = declarative_base()

#Creating a Class of Student to make one-to one relation with adhaar number
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    adhaar = relationship("Adhaar",back_populates = 'student',uselist=False)

class Adhaar(Base):
    __tablename__ = 'adhaars'
    id = Column(Integer,primary_key = True)
    adhaar_no = Column(Integer)
    student = relationship("Student",back_populates="adhaar")
    users_id = Column(Integer, ForeignKey('students.id'))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

abijith_card = Adhaar(adhaar_no = 123456)
abhilash_card = Adhaar(adhaar_no = 34456)

abijith = Student(name = 'abijith')
abhilash = Student(name = 'abhilahs')

abijith.adhaar = abijith_card
abhilash.adhaar = abhilash_card

session.add_all([abijith,abhilash])
session.commit()