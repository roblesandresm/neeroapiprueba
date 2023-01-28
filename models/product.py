from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String)
    tipo = Column(Integer)
    state = Column(Integer)

    briefcases = relationship("briefcase", secondary='briefcase_product')