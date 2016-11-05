from wut4lunch.models import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


class Lunch(Base):
    __tablename__ = 'lunch'
    id = Column(Integer, primary_key=True)
    submitter = Column(String(63))
    food = Column(String(255))