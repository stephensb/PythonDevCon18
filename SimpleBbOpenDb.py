#!/usr/bin python3.6
import sqlalchemy
import cx_Oracle
from sqlalchemy import create_engine

USER = ''
PASS = ''
IP = ''
PORT = ''
DB = ''
DEBUG = True

engine = create_engine(
    # "oracle://{0}:{1}@{2}:{3}/{4}".format(USER, PASS, IP, PORT, DB), # traditional str.format()
    f"oracle://{USER}:{PASS}@{IP}:{PORT}/{DB}", # new in 3.6!
    echo=DEBUG
)
conn = engine.connect()
result = conn.execute("select * from BBLEARN.users where rownum <= 1")
for row in result:
    print(row)
conn.close()
