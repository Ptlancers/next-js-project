from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, CheckConstraint
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class SectionCode(Base):
    __tablename__ = "section_codes"
    id = Column(Integer, primary_key=True)
    section_code = Column(String, default="")
    unique_registration_number = Column(String, default="")
    date_insurance_of_urn = Column(String, nullable=False)

    users = relationship("User", back_populates="section")
    receipts = relationship("Receipt", back_populates="section")


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    section_id = Column(Integer, ForeignKey('section_codes.id'))
    created_at = Column(DateTime, default=datetime.now)

    section = relationship("SectionCode", back_populates="users")


class Receipt(Base):
    __tablename__ = 'receipts'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    section_id = Column(Integer, ForeignKey('section_codes.id'))
    donor_registration_number = Column(String)
    receipt_number = Column(String)
    unique_identification_number = Column(String)
    address = Column(String)
    donation_type = Column(String)
    mode_of_receipt = Column(String)
    transaction_id = Column(String)
    donated_amount = Column(String)
    donated_amount_letter = Column(String)
    __table_args__ = (
        CheckConstraint('donated_amount != ""', name='check_nonempty_donated_amount'),
    )

    section = relationship("SectionCode", back_populates="receipts")
