import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


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





# creating multiple data into 1 graph


#3 data plot in one chart

  
N = 3
ind = np.arange(N) 
width = 0.25
  
xvals = [8, 9, 2]
bar1 = plt.bar(ind, xvals, width, color = 'r')
  
yvals = [10, 20, 30]
bar2 = plt.bar(ind+width, yvals, width, color='g')
  
zvals = [11, 12, 13]
bar3 = plt.bar(ind+width*2, zvals, width, color = 'b')
  
plt.xlabel("Dates")
plt.ylabel('Scores')
plt.title("Players Score")
  
plt.xticks(ind+width,['2021Feb01', '2021Feb02', '2021Feb03'])
plt.legend( (bar1, bar2, bar3), ('Player1', 'Player2', 'Player3') )
plt.show()











#2data plot in one  chart

import numpy as np 
import matplotlib.pyplot as plt 
  
X = ['Group A','Group B','Group C','Group D']
Ygirls = [10,20,20,40]
Zboys = [20,30,25,30]
  
X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, Ygirls, 0.4, label = 'Girls')
plt.bar(X_axis + 0.2, Zboys, 0.4, label = 'Boys')
  
plt.xticks(X_axis, X)
plt.xlabel("Groups")
plt.ylabel("Number of Students")
plt.title("Number of Students in each group")
plt.legend()
plt.show()








# 