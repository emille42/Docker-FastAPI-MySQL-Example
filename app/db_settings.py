import sqlalchemy as db
import os

config = {
    'host': os.environ['DB_HOST_NAME'],
    'port': 3306,
    'user': os.environ['DB_USER_NAME'],
    'password': os.environ['DB_PASSWORD'],
    'database': os.environ['DB_NAME']
}
db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
