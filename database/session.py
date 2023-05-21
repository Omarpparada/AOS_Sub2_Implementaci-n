from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




DATABASE = f"mysql+pymysql://root:root@127.0.0.1:3306/vehiculos"

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
