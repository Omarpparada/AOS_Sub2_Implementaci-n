from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




DATABASE = f"mysql+pymysql://{database_settings.SQL_USER}:{database_settings.SQL_PASSWORD}@{database_settings.SQL_HOST}/{database_settings.SQL_DATABASE}"

engine = create_engine(
    DATABASE,
    echo=False,
    pool_recycle=3600,
    pool_size=10,
    max_overflow=0
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
