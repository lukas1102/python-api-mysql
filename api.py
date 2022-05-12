from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from mysql.connector import Error


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
                record = mycursor.fetchone()
                return {"data": record }
        except Error as e:
            print("Error while connection to MySQL",e)

    def post(self):
        return {"data": "Posted"}

api.add_resource(User, "/")

if __name__ == "__main__":
	app.run(debug=True, port=5001)