from sqlalchemy import (MetaData, Table, Column, ForeignKey,
                        Integer, String, Boolean, DateTime, UniqueConstraint, Index)

metadata = MetaData()

users = Table(
    'users', metadata,

    Column('name', String(64), nullable=False),
    Column('surname', String(64), nullable=False),
    Column('login', String(64), nullable=False, unique=True, primary_key=True),
    Column('password', String(128), nullable=False),
    Column('birthdate', DateTime, nullable=False)

)

rights = Table(
    'rights', metadata,

    Column('user_login', String(64), ForeignKey('users.login', ondelete='CASCADE'), primary_key=True),
    Column('blocked', Boolean, default=False),
    Column('admin', Boolean, default=False),
    Column('readonly', Boolean, default=True)
    # UniqueConstraint("admin", "readonly", name="uniq rights level constraint")

)
