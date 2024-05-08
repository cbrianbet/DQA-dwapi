from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import datetime

from database import engine_dest

Base = declarative_base()


# Define dqadwapicentral table
class DQADwapicentral(Base):
    __tablename__ = "dqadwapicentral"

    id = Column(Integer, primary_key=True, index=True)
    mfl_code = Column(Integer, index=True)
    name = Column(String)  # Facility Name
    indicator = Column(String)  # Name of the query
    value = Column(String)  # Query results
    log_date = Column(DateTime, default=datetime.utcnow)
    dwapi_version = Column(String)  # Dwapi Version
    docket = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


# Define DWAPI duplicates table
class DQADwapiCentralPatientDuplicate(Base):
    __tablename__ = "DqaDwapiCentralPatientDuplicates"

    id = Column(Integer, primary_key=True, index=True)
    mfl_code = Column(Integer, index=True)
    name = Column(String)  # Facility Name
    number_of_dups = Column(Integer, nullable=True)
    log_date = Column(DateTime)
    reporting_date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)


# Define DWAPI PatientVisit Date created gt Date modified
class DQADwapiCentralPatientVisitsCheckDateCreatedModified(Base):
    __tablename__ = "DqaDwapiCentralPatientVisitsCheckDateCreatedModified"

    id = Column(Integer, primary_key=True, index=True)
    mfl_code = Column(Integer, index=True)
    name = Column(String)  # Facility Name
    number_anomalies = Column(Integer, nullable=True)
    log_date = Column(DateTime)
    reporting_date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)


# Define DWAPI PatientVisit meaningful visits
class DQADwapiCentralPatientMeaningfulVisits(Base):
    __tablename__ = "DqaDwapiCentralPatientMeaningfulVisits"

    id = Column(Integer, primary_key=True, index=True)
    mfl_code = Column(Integer, index=True)
    name = Column(String)  # Facility Name
    number_anomalies = Column(Integer, nullable=True)
    log_date = Column(DateTime)
    reporting_date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)


# Create the table in the destination database
Base.metadata.create_all(bind=engine_dest)


# Pydantic model for RabbitMQ message
class RabbitMQMessage(BaseModel):
    Facility: str
    MFL_Code: int
    Docket: str
    indicator_date: str
    Message: str
    log_date: str
    dwapi_version: str
