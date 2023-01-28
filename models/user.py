from config.database import Base
from sqlalchemy import Column, Integer, String

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    dni = Column(Integer)
    email = Column(String)
    password = Column(String)
    state = Column(Integer)