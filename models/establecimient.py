from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class EstablecimientModel(Base):
    __tablename__ = "establecimient"

    establecimient_id = Column(Integer, primary_key=True)
    briefcase_id = Column(Integer)
    name = Column(String)
    ciudad = Column(Integer)
    state = Column(Integer)