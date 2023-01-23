import numpy as np
import pandas as pd
import matplotlib.pylab as plt
# %matplotlib inline

# from matplotlib.pylab import rcParams



dataset = pd.read_csv("AirPassengers.csv")
dataset['Month'] = pd.to_datetime(dataset['Month'],infer_datetime_format=True)
# print(dataset.head())
indexedDataset = dataset.set_index('Month')

from datetime import datetime
# print(indexedDataset.tail())

plt.xlabel("Date")
plt.ylabel("No. of Passengers")
# plt.plot(indexedDataset)


#Rolling Statistics

rolmean = indexedDataset.rolling(window=12).mean()
rolstd = indexedDataset.rolling(window=12).std()
# print(rolmean , rolstd)

# actual=plt.plot(indexedDataset, color='red', label='Actual')
# mean_6=plt.plot(rolmean, color='green', label='Rolling Mean') 
# std_6=plt.plot(rolstd, color='black', label='Rolling Std')
# plt.legend(loc='best')
# plt.title('Rolling Mean & Standard Deviation')
# # plt.show(block=False)


#dickey fuller test

from statsmodels.tsa.stattools import adfuller

dftest = adfuller(indexedDataset['Passengers'] , autolag='AIC')
dfoutput = pd.Series(dftest[0:4] , index=["Test Statistics" , 'p-value', '#Lags used' , 'No of Observations Used'])

for key , value in dftest[4].items():
    dfoutput['Critical Value(%s)'%key] = value
print(dfoutput)
