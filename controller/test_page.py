# browser => controller => model
#localhost:5000/test => test_page.py => test_page_model
# controller => routing
# model => business logic
from app import app
from model.test_page_model import test_page_model

# making the object of test_page_model class
test_page_model_obj = test_page_model() 

@app.route("/test")
def test_page():
    print("This is test page. made in different file")
    return test_page_model_obj.test_page_model_fn() 