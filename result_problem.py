class Result():
    
    dt = {
          'A':88,
          'B':71,
          'C':84,
          'D':95,
          'E':60,
          'F':89
          }
        
    def add_rslt(self, student = ' ', marks=0):
        self.dt[student] = marks


class Student(Result):
    def sho_rslt(self , student):
        print(student , 'got' , self.dt[student],'marks')


obj = Student()
obj.add_rslt('G',85)
obj.add_rslt('H',67)

for i in ['A','B','D','F','H']:
    obj.sho_rslt(i)