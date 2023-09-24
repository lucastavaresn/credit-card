from sqlalchemy import create_engine
from sqlalchmey.orm import sessionmaker
from sqlalchmey.ext.declarative import declarative_base

URL_DATABASE = 'postgresql://postgres:postgres!localhost:5432/maisTodos'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


        
