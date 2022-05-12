from pkg_resources import require
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from mysql.connector import Error

users_put_args = reqparse.RequestParser()
users_put_args.add_argument("username",type=str,help="username is required",required=True)
users_put_args.add_argument("pwd",type=str,help="password is required", required=True)

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    pwd = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"User(name = {name}, pwd = {pwd})"
mydb = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "example",
            database = "users"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
record = mycursor.fetchone()
if record is None:
    mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), pwd VARCHAR(255))")


class User(Resource):
    def get(self):
        try:
            if mydb.is_connected():
                mycursor.execute("SELECT * FROM users")
                record = mycursor.fetchall()
                return {"data": record }
        except Error as e:
            print("Error while connection to MySQL",e)

    def put(self):
        args = users_put_args.parse_args()
        sql = "INSERT INTO users (name,pwd) VALUES (%s, %s)"
        val = (args["username"], args["pwd"])
        mycursor.execute(sql,val)
        mydb.commit()
        return {"user:" :args["username"] }, 201

api.add_resource(User, "/users")

if __name__ == "__main__":
	app.run(debug=True, port=5001)