from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

class TestModel(Base):

    __tablename__ = "people"

    id = Column(UUID, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)