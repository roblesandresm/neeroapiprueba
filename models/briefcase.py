from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class BriefcaseModel(Base):
    __tablename__ = "briefcase"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    state = Column(Integer)

    products = relationship("products", secondary='briefcase_product')