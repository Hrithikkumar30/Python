import pandas as pd
from matplotlib import pyplot as plt


data = pd.read_csv("C:/Users\hrith\Downloads/csv_data.csv" , 
                   names=['Id','Names','Price','Sales','Brand'],
                   skiprows=(1))

# plt.plot(data['Id'] , data['Sales'] , '.c',
#          markersize = 22)   #using '.c/-/+' we can define what will be the markersign of the our plot and markersize is used to give the size of markersign
plt.xlabel('x-axis') #use to give name of lable of x axis

plt.ylabel('Y-axix')#use to give name of lable of y axis

plt.bar(data['Id'] , data['Sales'] )





dt = {

'ProductA':[27,15,34,22,27,13,21],

'ProductB':[56,51,41,55,49,56,44],

'ProductC':[32,22,19,37,32,54,31],

'ProductE':[21,40,17,26,31,33,29],

'ProductF':[44,32,25,25,44,40,38]

}



sales = pd.DataFrame(data=dt, index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

print(sales)