# -*- coding: utf-8 -*-
from typing import Generator
# DBへの接続設定
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
# from sqlalchemy.pool import NullPool

# 接続したいDBの基本情報を設定
user_name = "admin"
password = "password"
host = "db"  # docker-composeで定義したMySQLのサービス名
database_name = "kintai_db"

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user_name,
    password,
    host,
    database_name,
)

# DBとの接続
ENGINE = create_engine(
    DATABASE,
    # path = "db://admin:password@localhost:3306/db??charset=utf8",
    # encoding="utf-8",
    echo=True
)

# Sessionの作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)

# modelで使用する
Base = declarative_base()
# DB接続用のセッションクラス、インスタンスが作成されると接続する
# Base.query = session.query_property()

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()