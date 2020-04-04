 from sqlalchemy.ext.declarative import declarative_base
 from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)