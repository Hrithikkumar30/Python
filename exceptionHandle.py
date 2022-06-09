# try:
#     num1 = int(input('number1_'))
#     num2 = int(input('number2_'))
#     print = ('quotinet:' + str(num1/num2))
# except ZeroDivisionError:
#     print("0 cannot be divisor")
# except ValueError:
#     print('Enter number')
# except:
#     print('something went wrong')




class ZeroCubeError(Exception):
    '''0 can not be passed as a cube'''

class Cube():
    def __init__(self, num) -> None:
        num = int(num)
        if num!=0:
            self.qub = num**3
        else:
            raise ZeroCubeError



try:
    num = Cube(input('enter number_'))
    print(num.qub)
    
except ZeroCubeError:
    print(ZeroCubeError.__doc__)
except:
    print('something went wrong')
finally:
    print('execution completed')

