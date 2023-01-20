"""Given an integer n, return a string array result where:

result[i] == “FizzBuzz” if i is divisible by 3 and 5.
result[i] == “Fizz” if i is divisible by 3.
result[i] == “Buzz” if i is divisible by 5.
result[i] == i in any other case.
    """

def FizzBuzz(n:int) -> list :  
    
# n = int(input('enter any number'))

    arr =[]
    for i in range(1,n+1):
        if i %3==0 and i % 5==0:
            arr.append('FizzBuzz')
            continue
        elif i%3==0:
            arr.append('Fizz')
            continue
        elif i%5==0:
            arr.append('Buzz')
            continue
        else:
            arr.append(str(i))

    return arr

for n in [3,5,15]:
    
    print(f"FizzBuzz(n={n}) = {FizzBuzz(n)}")

