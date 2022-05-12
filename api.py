from pkg_resources import require
from flask import Flask, request, abort
from flask_restful import Api, Resource, reqparse
import mysql.connector
from mysql.connector import Error
import os

users_put_args = reqparse.RequestParser()
users_put_args.add_argument("username",type=str,help="username is required",required=True)
users_put_args.add_argument("pwd",type=str,help="password is required", required=True)

app = Flask(__name__)
api = Api(app)

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
        database = os.environ['SQL_DB']
    else:
        database = "users"
except KeyError:
    database = "users"

mydb = mysql.connector.connect(
            host = hostname,
            user = usr,
            password = pwd,
            database = database
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
record = mycursor.fetchone()
if record is None:
    mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), pwd VARCHAR(255))")


class User(Resource):
    def get(self):
        print("reached get method")
        try:
            if mydb.is_connected():
                mycursor.execute("SELECT * FROM users")
                record = mycursor.fetchall()
                return {"data": record }
        except Error as e:
            abort(500,"Error while connection to MySQL")

    def put(self):
        print("reached put method")
        try:
            args = users_put_args.parse_args()
            sql = "INSERT INTO users (name,pwd) VALUES (%s, %s)"
            val = (args["username"], args["pwd"])
            mycursor.execute(sql,val)
            mydb.commit()
            return {"user:" :args["username"] }, 201
        except Error as e:
            abort(500,"Error while connection to MySQL")

api.add_resource(User, "/users")

if __name__ == "__main__":
	app.run(debug=False, port=5000)