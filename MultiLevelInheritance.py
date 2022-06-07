# MultiLevel InheritNCE
""" Multilevel Inheritance occurs when a class extends a class 
 that extends another class"""

# class Coder():
#     def code (self):
#         print('coding')

# class Pythonner(Coder):
#     def py_code(self):
#         print('code in python')

# class Django(Pythonner):
#     def web_dev (self):
#         print('new.html@ django')

# web = Django()
# web.code()
# web.py_code()
# web.web_dev()   





# Multiple Inheritance
""" When a class is derived from more than one base class it is 
 called multiple Inheritance"""

class Coder():
    def __init__(self) -> None:
        self.name = input('Name_')
class Pythonner():
    def __init__(self) -> None:
        self.works = input('Works')

class WevDev(Coder , Pythonner):
    def __init__(self) -> None:
        Coder().__init__(self)
        Pythonner.__init__(self)
    def start_new(slef):
        print('new.html@Django')

web= WevDev()
web.start_new()