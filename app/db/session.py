from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os.path

SQLITE_DB_URL = f"sqlite:///{os.path.dirname(os.path.abspath(__file__))}/CBS_test.sqlite"

engine = create_engine(
    SQLITE_DB_URL, echo=True, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
