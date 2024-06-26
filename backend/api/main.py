from fastapi import FastAPI
from typing import List
from starlette.middleware.cors import CORSMiddleware  # CORSエラーを回避
from .db import SessionLocal
from .model import UserTable, User

app = FastAPI()

# CORSエラーを回避
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# test GET　responseが返っているか確認
@app.get('/hello')
async def hello():
    response = {
        'message': 'ようこそ 勤怠管理システムへ!'
    }
    return response

# テーブルにいる全ユーザ情報を取得 GET
@app.get("/users")
def read_users():
    db = SessionLocal()
    users = db.query(UserTable).all()
    return users

# idにマッチするユーザ情報を取得 GET
@app.get("/users/{user_id}")
def read_user(user_id: int):
    db = SessionLocal()
    user = db.query(UserTable).filter(UserTable.id == user_id).first()
    return user

# ユーザ情報を登録 POST
@app.post("/user")
async def create_user(name: str, age: int):
    user = UserTable()
    user.name = name
    user.age = age
    db = SessionLocal()
    db.add(user)
    db.commit()

# 複数のユーザ情報を更新 PUT
@app.put("/users")
async def update_users(users: List[User]):
    db = SessionLocal()
    for new_user in users:
        user = db.query(UserTable).\
            filter(UserTable.id == new_user.id).first()
        user.name = new_user.name
        user.age = new_user.age
        db.commit()