import numpy as np

#1-D arrays
# ar = np.array([12,34,56])
# print(ar)

# #2-D arrays
# two_D_arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]],   ndmin =3) #ndmin is used to create a 2-D array with 3 rows and 3 columns 
# print(two_D_arr)


#concatinate array

arr =  np.array(
    [1,2,3]
)
Arr = arr+5

print(Arr) 


arr_1 =  np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr_1[0,1,2]) #print the value of the third element of the second row of the first column
print(arr_1)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

# print(arr)
    
print(arr1+arr2)


ar = np.array([[[1,2,3], [4,5,6]],
                [[1,2,3] ,[4,5,6]],
                [[1,2,3],[4,5,6]],

                [1,2,3],
                [2,3,4],
                [4,5,6]])
                

print(ar)