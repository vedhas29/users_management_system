# browser => controller => model
#localhost:5000/test => test_controller.py => test_controller_model.py
# controller => routing
# model => business logic

from app import app
from model.test_controller_model import test_controller_model



# making the object of test_page_model class to access fn of that class
test_controller_model_obj = test_controller_model()
@app.route('/test_controller')
def test_controller():
    print("This is test_controller")
    print("this is test_controller()")
    return test_controller_model_obj.test_controller_model_fn()