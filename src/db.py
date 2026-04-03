from sqlalchemy import Column, Float, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config.settings import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


class ForecastLog(Base):
    __tablename__ = "forecast_logs"

    id = Column(Integer, primary_key=True, index=True)
    month_index = Column(Integer, nullable=False)
    tla_tldds = Column(Float, nullable=False)
    tlep = Column(Float, nullable=False)
    predicted_flux_la_ldds = Column(Float, nullable=False)


def create_tables():
    Base.metadata.create_all(bind=engine)
