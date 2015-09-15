from sqlalchemy import Column, Integer, String
from my_poj.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unuque=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
    
    def __repr__(self):
        return '<User %r>' % (self.name)
