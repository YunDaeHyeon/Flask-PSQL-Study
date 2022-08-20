from calendar import day_name
from sqlite3 import connect
from xml.sax.handler import property_dom_node
import psycopg2
import json

with open('./secret.json', 'r', encoding='utf-8') as f:
    secret_data = json.loads(f.read())


conn = None
cursor = None

def connect():
    global conn, cursor
    dbname = secret_data.get('dbname')
    password = secret_data.get('password')
    user = secret_data.get('user')
    host = secret_data.get('host')
    port = secret_data.get('port')

    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def is_login(user_id, user_pwd):
    connect() # DB 연결
    # """ """ 큰따옴표 3개는 긴 쿼리를 작성할 때 사용
    # f는 포맷팅 방식으로, 
    cursor.execute(f"""
        SELECT * FROM Users WHERE email='{user_id}' and password='{user_pwd}'
    """)
    data = cursor.fetchone()
    close() # DB 해제
    return data

def likes(user_id):
    connect()
    cursor.execute(f"""
        INSERT INTO Likes
        VALUES('{user_id}')
        RETURNING 1
    """)
    data = cursor.fetchone()
    print(data)

    close()
# insert into Users(email, password) values('test@naver.com', '1234')
# json과 hip, 전역변수, 지역변수의 관계 학습