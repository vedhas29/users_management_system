# browser => controller => model
#localhost:5000/test => test_controller.py => test_controller_model.py
# controller => routing
# model => business logic
# model files are used to write business logic

class test_controller_model:
    def test_controller_model_fn(self):
        print("this is test_controller_model_fn")
        return "test_controller_model_fn()"



# test_controller_model.py => test_controller.py => browser