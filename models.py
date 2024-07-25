from __future__ import annotations

import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP

from database import Base


class History(Base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    user_ip = Column(String, index=True, nullable=False)
    city_name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
