from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from CF.app.db import Base


class Records(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    person = Column(Text, nullable=False)
    data_id = Column(Integer, ForeignKey("data.id"))
    c = relationship("Data", back_populates="p")
