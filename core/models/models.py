from db import Base
from sqlalchemy import Column,Float,String,Integer,ForeignKey,DateTime,Date
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, autoincrement = True)
    username = Column(String)
    hashed_password = Column(String)
    email = Column(String)
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship('Role')

class Budget(Base):
    __tablename__ = 'budgets'

    id = Column(Integer, primary_key = True, autoincrement = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category')
    amount = Column(Float)
    start_date = Column(DateTime, default = datetime.now())
    end_date = Column(DateTime)

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    type = Column(String)

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, autoincrement = True)
    amount = Column(Float)
    description = Column(String)
    type = Column(String, nullable = True)
    date = Column(Date)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category')
    account_id = Column(Integer, ForeignKey('accounts.id'))
    account = relationship('Account')

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, autoincrement = True)
    name = Column(String)
    type = Column(String)
    balance = Column(Float)
    currency = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')
    created_at = Column(DateTime, default = datetime.now())

class Report(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')
    description = Column(String)
    created_at = Column(DateTime, default = datetime.now())

class Goal(Base):
    __tablename__ = 'goals'

    id = Column(Integer, autoincrement = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')
    target_amount = Column(Float)
    current_amount = Column(Float)
    description = Column(String)
    created_at = Column(DateTime, default = datetime.now())


