#code for adding pairs in a list till end

# class SumPair ():
#     def __init__(self , lst):
#         self.List = lst
#         self.List_len = len(lst)
#         self.i1=0
#         self.i2=1
#     def __iter__(self): # helps for iterating the list
#         return self

#     def __next__(self):
#         if self.i2 == self.List_len:
#             raise StopIteration
#         else:
#             self.sum_pair = self.List[self.i1]+self.List[self.i2]
#             self.i1 +=1
#             self.i2 +=1
#             return self.sum_pair


# obj = SumPair([12,34,5,67,89,12])

# print(obj.List_len)
# for ele in obj :
#     print(ele)
# class Algebra():
#   def __init__(self, n ):
#     self.val = n
#   def incrse(self):
#     self. val += 1
 
# num = Algebra(12)
# num.incrse()
# print(num.val)

# class LenVal ():
#     def __init__(self, lst):
#         self.List = lst
#         self.len_list = len(self.List)
#     def sho_val(self):
#         return self.len_list

# obj1 = LenVal([1,9,4,2,6])
# print(obj1.len_list)


class LenVal ():
    def __init__( ):
       pass
    def sho_val(self , lst ):
        self.List = lst
        self.len_list = len(self.List)
        return self.len_list
obj1 = LenVal()
print(obj1.sho_val([1,9,4,2,6]))

