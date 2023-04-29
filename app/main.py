import sqlalchemy as db
from db_settings import *
from schemas import User
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

app = FastAPI()
engine = db.create_engine(connection_str)


@app.get("/get_user")
def get_user(user_id: int):
    connection = engine.connect()
    metadata = db.MetaData()
    metadata.reflect(bind=engine)
    table_users = metadata.tables['Users']

    stmt = db.select(table_users.columns.login).where(table_users.columns.ID == user_id)
    result = connection.execute(stmt)
    connection.close()
    if result.rowcount == 0:
        return {"message": f"User with id {user_id} don't exist"}
    else:
        rows = []
        for row in result:
            rows.append(row[0])
        return {"message": rows}


@app.post('/create_user')
def create_user(user: User):
    json_obj = jsonable_encoder(user)
    login = json_obj["login"]
    password = json_obj['password']
    connection = engine.connect()
    metadata = db.MetaData()
    metadata.reflect(bind=engine)
    table_users = metadata.tables['Users']

    stmt = db.select(table_users).where(table_users.columns.login == login)
    result = connection.execute(stmt)
    if result.rowcount != 0:
        connection.close()
        return {"message": f"User {login} already exist"}
    else:
        stmt = db.insert(table_users).values(login=login, password=password)
        connection.execute(stmt)
        connection.commit()
        connection.close()
        return {"message": f"Successfully created user: {login}"}


@app.post('/delete_user')
def delete_user(user_id: int):
    connection = engine.connect()
    metadata = db.MetaData()
    metadata.reflect(bind=engine)
    table_users = metadata.tables['Users']
    stmt = db.delete(table_users).where(table_users.columns.ID == user_id)
    result = connection.execute(stmt)
    connection.commit()
    connection.close()
    if result.rowcount == 0:
        return {"message": "User don't exist"}
    else:
        return {"message": f"Successfully deleted user: {user_id}"}


@app.post('/update_password')
def update_password(login: str, new_password: str):
    connection = engine.connect()
    metadata = db.MetaData()
    metadata.reflect(bind=engine)
    table_users = metadata.tables['Users']
    stmt = db.update(table_users).where(table_users.columns.login == login).values(password=new_password)
    result = connection.execute(stmt)
    connection.commit()
    connection.close()
    if result.rowcount == 0:
        return {"message": "Error"}
    else:
        return {"message": f"Successfully updated password for: {login}"}
