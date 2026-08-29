# database.py
# ------------------------------------------------------
# Ei file er kaj: Database er sathe connection banano.
# SQLite use kora hocche karon eta file-based, kono extra
# server lagbe na. Real project e PostgreSQL/MySQL use korbe,
# khali "SQLALCHEMY_DATABASE_URL" change korle hobe.
# ------------------------------------------------------

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL — "app.db" naam e ekta sqlite file toiri hobe
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# Engine — DB er sathe actual connection handle
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal — protyekta request er jonno ekta DB session toiri hobe
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base — shob model class ei Base theke inherit korbe
Base = declarative_base()


# Dependency function — routers e ei function call kore DB session pawa jay
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
