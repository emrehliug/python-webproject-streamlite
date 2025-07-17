from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLSERVER_DATABASE_URL = "mssql+pyodbc://username:password@server/database?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(SQLSERVER_DATABASE_URL, echo=True)

SessionDbGeral = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 


def get_db():
    db = SessionDbGeral()
    try:
        yield db
    finally:
        db.close()