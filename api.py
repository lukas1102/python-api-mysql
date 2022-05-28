from pkg_resources import require
from flask import Flask, request, abort
from flask_restful import Api, Resource, reqparse
import mysql.connector
from mysql.connector import Error
import os

users_put_args = reqparse.RequestParser()
users_put_args.add_argument("name1",type=str,help="username is required",required=True)
users_put_args.add_argument("name2",type=str,help="password is required", required=True)

app = Flask(__name__)
api = Api(app)


class Mysql_Connection():
    def __init__(self):
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

        self.mydb = mysql.connector.connect(
                    host = hostname,
                    user = usr,
                    password = pwd,
                    database = database
        )
        self.mycursor = self.mydb.cursor()
        #self.mycursor.execute("SHOW TABLES")
        #record = self.mycursor.fetchone()
        #if record is None:
        #    self.mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), pwd VARCHAR(255))")
        
    def connect_reading(self,Statement):
        try:
            if self.mydb.is_connected():
                self.mycursor.execute(Statement)
                record = self.mycursor.fetchall()
                self.mydb.close()
                return record 
            else:
                abort(500, "something went wrong")
        except Error as e:
            abort(500,"Error while connection to MySQL",e)

    def connect_writing(self,n1,n2):
        try:
            sql = "INSERT INTO users (name,pwd) VALUES (%s, %s)"
            val = (n1, n2)
            self.mycursor.execute(sql,val)
            sql = "SELECT id FROM users WHERE name=%s and pwd=%s"
            self.mycursor.execute(sql,val)
            record = self.mycursor.fetchall()

            sql = "INSERT INTO invoice (user_id,creation_date) VALUES (%s, (SELECT current_timestamp))"
            for x in record:
                val = (x)
                self.mycursor.execute(sql,val)
            
            self.mydb.commit()
            self.mydb.close()
        except Error as e:
            abort(500,"Error while connection to MySQL")

class User(Resource):
    def get(self):
        print("reached get method")
        sql = Mysql_Connection()
        return {"data: ": sql.connect_reading("SELECT * FROM users") }

        
    def put(self):
        print("reached put method")
        sql = Mysql_Connection()
        try:
            args = users_put_args.parse_args()
            sql.connect_writing(args["name1"],args["name2"])
            
            return {"user:" :args["name1"] }, 201
        except Error as e:
            abort(500,"Error while connection to MySQL")
        
class UserKV(Resource):
    def get(self):
        pass


api.add_resource(User, "/")
api.add_resource(UserKV, "/kv")

if __name__ == "__main__":
	app.run(debug=False, port=5001, host='0.0.0.0')