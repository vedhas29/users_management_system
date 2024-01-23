from flask import Flask
from decouple import config

app = Flask(__name__)
# print("HI")

@app.route("/")
def welcome_page():
    print("HELLO WORLD")
    return "HELLO WORLD"


from controller import *
# import controller.test_page as test_page
# import controller.test_controller as test_controller
# @app.route("/test")
# def test_page():
#     print("THIS IS TEST PAGE")
#     return "THIS IS TEST PAGE"

