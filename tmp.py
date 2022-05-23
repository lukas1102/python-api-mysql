import os

import mysql.connector
from mysql.connector import Error

try:
    if os.environ['SQL_HOST']:
        hostname = os.environ['SQL_HOST']
    else:
        hostname = "127.0.0.1"
except KeyError:
    hostname = "127.0.0.1"

try:
    if os.environ['SQL_USER']:
        usr = os.environ['SQL_USER']
    else:
        usr = "root"
except KeyError:
    usr = "root"

try:    
    if os.environ['SQL_PWD']:
        pwd = os.environ['SQL_PWD']
    else:
        pwd = "example"
except KeyError:
    pwd = "example"

try:
    if os.environ['SQL_DB']:
        db = os.environ['SQL_DB']
    else:
        db = "users"
except KeyError:
    db = "users"

mydb = mysql.connector.connect(
            host = hostname,
            user = usr,
            password = pwd,
            database = db
)

try:
    mycursor = mydb.cursor()

    if mydb.is_connected():
        mycursor.execute("SHOW tables")
        record = mycursor.fetchall()
        print("sucessfull connection \n")
        for x in record:
            print(x)
    else:
        print("something else wrent wrong")
except Error as e:
        print("Error while connection to MySQL",e)