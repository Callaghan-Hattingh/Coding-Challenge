from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship
from CF.app.db import Base


class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    json = Column(Text, nullable=False)
    p = relationship("Records", back_populates="c")
