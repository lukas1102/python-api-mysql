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
        db = "invoices"
except KeyError:
    db = "invoices"

mydb = mysql.connector.connect(
            host = hostname,
            user = usr,
            password = pwd,
            database = "invoices"
)

try:
    mycursor = mydb.cursor()

    if mydb.is_connected():
        mycursor.execute("SHOW TABLES")
        record = mycursor.fetchall()
        if not record or record is None:
            #mycursor.execute("CREATE TABLE users (id BIGINT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), pwd VARCHAR(255))")
            mycursor.execute("CREATE TABLE invoice (invoice_id BIGINT , user_id BIGINT , creation_date TIMESTAMP not null, price INT, PRIMARY KEY(invoice_id,user_id))")
            mydb.commit()
            mydb.close()
            print("successful connection \n")
        for x in record:
            print(x)
        #print(record)
    else:
        print("something else wrent wrong")
except Error as e:
        print("Error while connection to MySQL",e)