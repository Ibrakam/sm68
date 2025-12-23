from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#какой тип бд будем использовать(sqlite3, postgres)
SQL_DATABASE = "sqlite:///sm68.db"

#создаем бд
engine = create_engine(SQL_DATABASE)

#Cоздаем сесси
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise
    finally:
        db.close()



