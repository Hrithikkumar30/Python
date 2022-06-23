import pandas as pd

data = pd.read_csv("C:/Users\hrith\Downloads/csv_data.csv" , 
                   names=['Id','Names','Price','Sales','Brand'],
                   skiprows=(1)) #skip row is used to skip the no of rows from the top of the table or chart
print(data)


print(data.isnull()) #isnull method is used to check if any item is null or nan if yes then it will return true otherwise false

data.fillna(0) 

#fillna mehtod is used to fill the null or nan value
data.pad()
data.dropna() #dropna method is used to drop the null row from the csv or datafiel

# print(data.drop([4,2])) #drop method is used to drop the row which we want to drop by specifing its index value
# del data['Sales']  #del method is used to delte  a specify column which we wants
print(data)

data_1 = data.drop(columns=['Price','Sales']) #this method is used to drop particular column without deleting it permanently
print(data_1)
print(data)