from enum import unique
from os import makedirs


# def product(): #define the product
#     prod =  12*35
#     print(prod)

# product() #execute the function

# def addition(a,b):
#     print(a+b)

# addition(34,78)

# def result(name , marks):
#     print("Name:" + str(name))
#     print("marks:" + str(marks))

# result("Hrithik" , 56) #positional argument
# result(name ="Hrithik" , marks= 56) #named argument


# def result(name = "None" , marks= None):
#     if name != "None" or marks != None:
#         print("Name:" + str(name))
#         print("marks:" + str(marks))

# result( )


# def add (*n):# for printing any count of numbers
#     sm = 0
#     for num in n :
#         sm += num
#     print(sm)

# add(1,2,3,4,5,5)


# def info(**kw): #we can pass any number of argument or no argument
#     for k,v in kw.items():
#         print(k,":" ,v)
        
# info( name ='jake',age = 15,
#         marks= 78)



#program to print till sum smallest decimal places

# def sum_r (*n):
#     sm = 0
#     d = []

#     for num in n:
#         sm += num
#         Num = str(num).split(".")
#         d.append(len(Num[1]))

#     min_d = min(d)
#     return round (sm , min_d)

# print(sum_r(12.561,12.567,34.456,54.5678))

#we use pass keyword to avoid error when we have to leave function to write code in future
# def function():
#     pass



#lambda functon used for fast action. 

# sub = lambda n,m: n-m 

# print (sub(19,4))


#creating dublicate remover from list using function

# list_1 = [12,3,4,55,12,3,4,56,7,3,4]
# def remove_dub(l):
#     uniq =set(l)
#     return list(uniq)

# print(list_1)
# print(remove_dub(list_1))


# lst = [ 5, 6, 7, 23 ,12 ,3, 3, 4 ,5, 12, 34]
# def dsort(l):
#     lst.sort()

    
#     lst.reverse()
#     return lst
#     # print(r)
# print(dsort(lst))


Str1 = 'Desserts'
Str2 = "Live" 
Str3 = 'Pals'
Str4 = 'God'
Str5 = 'Raw'
lst = []
lst_1 = [ ]

def str_rev(Str1):
    lst = list(Str1)
    return lst


    # for i in lst:
    #     a = lst.remove()
    #     a = lst_1.append()
    
print(str_rev(Str1))