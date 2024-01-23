
from app import app
from model.users_controller_model import users_controller_model
from flask import request

users_controller_model_obj = users_controller_model()
@app.route("/users/get")
def users_controller_for_GET():
    print("in users_controller")
    print ("users_controller() working")
    return users_controller_model_obj.GET_USERS()

@app.route("/users/post", methods = ["POST"])
def users_controller_for_POST():
    print("in user_controller_post")
    print("working")
    # get the data from postman
    print(request.form)
    data_to_fn = request.form
    return users_controller_model_obj.POST_USERS(data_to_fn)


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