# browser => controller => model
#localhost:5000/test => test_page.py => test_page_model
# controller => routing
# model => business logic
# model files are used to write business logic
class test_page_model:
    def test_page_model_fn(self):
        print("We are test_page_model")
        return "We are in test_page_model"