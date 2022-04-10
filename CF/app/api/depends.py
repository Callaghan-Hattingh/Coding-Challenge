from sqlalchemy.orm import sessionmaker
from ..db import engine, Base


def create_db_and_tables():
    Base.metadata.create_all(engine)


DBSession = sessionmaker(bind=engine)
session = DBSession()
