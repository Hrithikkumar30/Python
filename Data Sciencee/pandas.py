import pandas as pd
import numpy as np
# sr = pd.Series([12,33,44,56] ,index=('a','b','c','d'))  #index is used to give the name to the series
# print(sr)


# #converting numpy array to pandas series

# arr = np.array([12,33,44,56])

# series = pd.Series(arr , index=('a','b','c','d'))
# print(series)

# #slicing in pandas

# series1 = pd.Series([22,23,34,66] , index=('a','b','c','d'))
# print(series1.loc['b']) #LOC is used to slice the series based on the index given by user
# print(series1.iloc[1]) #ILOC is used to slice the series from integer index which is by defaut python


# #creating dataframe using numpy and pandas

# ar = np.array([[10,20,30,40],
#               [40,50,60,70]])

# df = pd.DataFrame(data=ar , index=('a','b'), columns=('x','y','z','w'))  #data is the data to be stored in the dataframe, dataframe is used to store the data in a table format
# print(df)

# #slicing in dataframe
# print(df.values[1,3])




import matplotlib.pyplot as plt
  
# creating dataframe
df = pd.DataFrame({
    'Name': ['John', 'Sammy', 'Joe'],
    'Age': [45, 38, 90],
    'Height(in cm)': [150, 180, 160]
})
  
# creating subplots and plotting them together
ax = plt.subplot()
ax.bar(df["Name"], df["Height(in cm)"])
ax.bar(df["Name"], df["Age"], color="maroon")



  
# creating dataframe
df = pd.DataFrame({
    'Name': ['John', 'Sammy', 'Joe'],
    'Age': [45, 38, 90],
    'Height(in cm)': [150, 180, 160]
})
  
# plotting Height
ax = df.plot(x="Name", y="Height(in cm)", kind="bar")
# plotting age on the same axis
df.plot(x="Name", y="Age", kind="bar", ax=ax, color="maroon")


df = pd.DataFrame({
    'Name': ['John', 'Sammy', 'Joe'],
    'Age': [45, 38, 90],
    'Height(in cm)': [150, 180, 160]
})
  
# plotting graph
df.plot(x="Name", y=["Age", "Height(in cm)"], kind="bar")