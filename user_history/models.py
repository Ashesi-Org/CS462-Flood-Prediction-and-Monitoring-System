from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserHistory(Base):
    __tablename__ = 'UserHistory'

    history_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    action = Column(String(255), nullable=False)
    action_time = Column(TIMESTAMP, default=func.now())
    details = Column(Text)
