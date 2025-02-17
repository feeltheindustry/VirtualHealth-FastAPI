"""Imports"""
from db import Base
from sqlalchemy import(
    DateTime,
    Date,
    Float,
    ForeignKey,
    Integer,
    String,

)
from sqlalchemy.orm import(
    relationship,
    mapped_column
)
from datetime import datetime

"""Database models"""

class Role(Base):
    __tablename__ = 'role'
    
    id = mapped_column(Integer, primary_key = True, index = True)
    name = mapped_column(String, unique = True, index = True) 

class User(Base):
    __tablename__ = 'user'

    id = mapped_column(Integer, primary_key = True, autoincrement = True)
    username = mapped_column(String)
    hashed_password = mapped_column(String)
    email = mapped_column(String)
    role_id = mapped_column(Integer, ForeignKey('roles.id'))
    role = relationship('Role')

class Budget(Base):
    __tablename__ = 'budget'

    id = mapped_column(Integer, primary_key = True, autoincrement = True)
    user_id = mapped_column(Integer, ForeignKey('users.id'))
    user = relationship('User')
    category_id = mapped_column(Integer, ForeignKey('categories.id'))
    category = relationship('Category')
    amount = mapped_column(Float)
    start_date = mapped_column(DateTime, default = datetime.now())
    end_date = mapped_column(DateTime)

class Category(Base):
    __tablename__ = 'category'

    id = mapped_column(Integer, primary_key = True)
    name = mapped_column(String)
    type = mapped_column(String)

class Transaction(Base):
    __tablename__ = 'transaction'

    id = mapped_column(Integer, autoincrement = True)
    amount = mapped_column(Float)
    description = mapped_column(String)
    type = mapped_column(String, nullable = True)
    date = mapped_column(Date)
    category_id = mapped_column(Integer, ForeignKey('categories.id'))
    category = relationship('Category')
    account_id = mapped_column(Integer, ForeignKey('accounts.id'))
    account = relationship('Account')

class Account(Base):
    __tablename__ = 'account'

    id = mapped_column(Integer, autoincrement = True)
    name = mapped_column(String)
    type = mapped_column(String)
    balance = mapped_column(Float)
    currency = mapped_column(String)
    user_id = mapped_column(Integer, ForeignKey('users.id'))
    user = relationship('User')
    created_at = mapped_column(DateTime, default = datetime.now())

class Report(Base):
    __tablename__ = 'report'

    id = mapped_column(Integer, primary_key = True)
    user_id = mapped_column(Integer, ForeignKey('users.id'))
    user = relationship('User')
    description = mapped_column(String)
    created_at = mapped_column(DateTime, default = datetime.now())

class Goal(Base):
    __tablename__ = 'goal'

    id = mapped_column(Integer, autoincrement = True)
    user_id = mapped_column(Integer, ForeignKey('users.id'))
    user = relationship('User')
    target_amount = mapped_column(Float)
    current_amount = mapped_column(Float)
    description = mapped_column(String)
    created_at = mapped_column(DateTime, default = datetime.now())


