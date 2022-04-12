# class Coder():#intialize class
#     def __init__(self , name) :
#         self.Name = name #class variable
#     def is_pythoneer(self):
#         if 'python' in self.language:
#             print(True)
#         else:
#             print(False)


# cd = Coder("")
# cd.language = ["python" , 'c'] #adding identifier to class outside
# cd.is_pythoneer()


# # print(cd.Name)


# class Python ():
#     name = 10
#     _age = 17 # _used for private variable no one can access
#     __pin = 7250 #highest protected by __
#     def __init__(self) :
#         pass
#     def python_code(self):
#         print("codin")

# obj = Python()
# print(obj._age)
# obj.python_code()
# # print(obj.__pin)  un executable because highly protected



from pickle import FALSE


class Progammer():
    def __init__(self , name) :
        self.Name = name

    def get_lang(self , lang):
        self.lang = lang

def python_progmer(lst):
        if 'python' in lst:
            print(True)
        else:
            print(False)

obj = Progammer("Hrithik")
obj.get_lang(['python' ,'c'])
python_progmer(obj.lang)


print(obj.lang)