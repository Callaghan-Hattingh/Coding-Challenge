from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from configparser import ConfigParser


Base = declarative_base()

cfg = ConfigParser()
cfg.read("database.ini")

user = cfg.get("postgresql", "user")
password = cfg.get("postgresql", "password")
dbname = cfg.get("postgresql", "dbname")
host = cfg.get("postgresql", "host")

pgsql_url = "postgresql://{}:{}@{}/{}".format(user, password, host, dbname)

sqlite_url = f"sqlite:///database.db"  # offline database

engine = create_engine(pgsql_url, echo=False)
