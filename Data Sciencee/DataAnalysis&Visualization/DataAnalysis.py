import pandas as pd

data = pd.read_csv("C:/Users\hrith\Downloads/csv_data.csv" , 
                   names=['Id','Names','Price','Sales','Brand'],
                   skiprows=(1))
data.fillna(0 , inplace=True) #this method is used to replace nan value in the dataf
print(data['Sales'])

data['Sales'].sum() # for adding/get the sum of the whole column
data['Sales'].min() # for getting minimum values of the particular column

#Getting mean median mode of the data
print(data['Sales'].mean())
print(data['Sales'].median())
print(data['Sales'].mode())

analytics = pd.DataFrame({'Total Sales' : data['Sales'].sum(),
                          'Average Sales': data['Sales'].mean(),
                          'Maximum Sales': data['Sales'].max()},
                         index=[1])
print(analytics)


#to describe the data
data.describe()