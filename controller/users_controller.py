
from app import app
from model.users_controller_model import users_controller_model
from flask import request
from wtforms import Form, StringField, validators,IntegerField
import asyncio
import aiomysql

class UserForm(Form):
    city = StringField('city', [validators.InputRequired(), validators.Length(min=1,max=50)])
    fullName = StringField('fullName', [validators.InputRequired(),validators.Length(min=1, max=250)])
    id = IntegerField('id', [validators.InputRequired()])

users_controller_model_obj = users_controller_model()
@app.route("/users/get")
async def users_controller_for_GET():
    print("in users_controller")
    print ("users_controller() working")
    return await users_controller_model_obj.GET_USERS()

@app.route("/users/post", methods = ["POST"])
def users_controller_for_POST():
    print("in user_controller_post")
    print("working")
    # get the data from postman
    print(request.form)
    # data_to_fn = request.form
    # validating data that is received from postman
    form  = UserForm(request.form)
    print(form.data)
    print(form.validate())
    if request.method == 'POST' and form.validate():
        data_to_fn = form.data
        return users_controller_model_obj.POST_USERS(data_to_fn)
    else:
        return {"message" : "Invalid data format"}

@app.route("/users/put", methods = ["PUT"])
def users_controller_for_PUT():
    print("in user_controller_put")
    # get data from postman
    print(request.form)
    data_to_fn = request.form
    return users_controller_model_obj.PUT_USERS(data_to_fn)


@app.route("/users/delete/<id>" , methods = ["DELETE"])
def users_controller_for_DELETE(id):
    print("in user_controller_DELETE")
    # # get data from postman
    # data_to_fn = request.form
    return users_controller_model_obj.DELETE_USER(id)

@app.route("/users/patch/<id>" , methods = ["PATCH"])
def users_controller_for_PATCH(id):
    print("In users_controller_PATCH")
    data_to_fn = request.form
    return users_controller_model_obj.PATCH_USER(id,data_to_fn)