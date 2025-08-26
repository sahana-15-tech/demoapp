# database.py
import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base, sessionmaker

DB_USER = os.getenv("DB_USER", "demo_user")
DB_PASS = os.getenv("DB_PASS", "demo_pass")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "demo_db")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

# Tables
class AppV1Data(Base):
    __tablename__ = "appv1_data"
    id = Column(Integer, primary_key=True, index=True)
    add_date = Column(DateTime, default=func.now())
    random_str = Column(String(255))

class AppV2Data(Base):
    __tablename__ = "appv2_data"
    id = Column(Integer, primary_key=True, index=True)
    add_date = Column(DateTime, default=func.now())
    random_str = Column(String(255))


def init_db():
    Base.metadata.create_all(bind=engine)
