import mysql.connector
import json
from decouple import config

class users_controller_model:
    def __init__(self):
        #connection establishment between sql and python
        try:
            self.db_connection = mysql.connector.connect(host=config('HOST'), user = config('USER'), password= config('PASSWORD') , database = config("DATABASE"))
            # autocommit is used so that we dont have to commit after every POST
            self.db_connection.autocommit=True
            print("Connection successfull")
            # cur=>cursor allows to interact with db by SQL queries via db_connection
            self.cur = self.db_connection.cursor(dictionary=True)
        except Exception as e:
            print("Exception while connecting with db" , e)


# GET API
    def GET_USERS(self):
        self.cur.execute("SELECT * FROM USERS")
        fetched_data = self.cur.fetchall()
        print("GET : ", fetched_data)
        print("in GET_USERS_fn()")
        if len(fetched_data)>0:
            return {"User details" : fetched_data} #returns as JSON
        # return json.dumps(fetched_data) #returns as text.html
        else:
            return {"message" : "NO DATA FOUND"}
     
# POST API
    def POST_USERS(self, data):
        self.cur.execute(f"insert into users (id, fullName, city) values ('{data['id']}', '{data['fullName']}', '{data['city']}')")
        print(data)
        for i in data:
            print(i, "=>" , data[i])
        return {"message":"data inserted"}
    
# PUT/UPDATE API
    def PUT_USERS(self, data):
        self.cur.execute(f"update users set  fullName = '{data['fullName']}', city = '{data['city']}' where id = {data['id']}")
        if self.cur.rowcount>0:
            return {"message":"Data UPDATED"}
        else:
            return {"message":"Nothing is updated"} 

# DELETE USER
    def DELETE_USER(self, id):
        self.cur.execute(f"delete from users where id = {id}")    
        if self.cur.rowcount>0:
            return {"message":f"User with {id} has been delete"}
        else:
            print("nothing to delete")
            return {"message" : "nothing to delete"}

# PATCH USER
# "update users set  fullName = '{data['fullName']}', city = '{data['city']}' where id = {data['id']}")
    def PATCH_USER(self, id, data):
        print(data)
        query = "update users set "
        for i in data:
            print(i, "=>" , data[i])
        print(query)
        for i in data:
            query = query + f"{i} = '{data[i]}',"
        print(query)
        query = query[:-1]
        query += f" where id = {id}"
        print(query)
        self.cur.execute(query)
        if self.cur.rowcount>0:
            return {"message":"DATA UPDATED SUCCESSFULLY"}
        else:
            return {"message" : "NOTHING TO UPDATE"}

# i => data[i]
# fullName => Roronoa Zoro
# city => wano