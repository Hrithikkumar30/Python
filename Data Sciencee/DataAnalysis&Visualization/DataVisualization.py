import pandas as pd

data = pd.read_csv("C:/Users\hrith\Downloads/csv_data.csv" , 
                   names=['Id','Names','Price','Sales','Brand'],
                   skiprows=(1))
# data.plot()

#for ploting bar graph
# data['Sales'].plot.bar()
# data['Price'].plot.bar()
data.drop(columns=['Id'],inplace = True)

data.plot.bar()
data.plot.bar(stacked=True) #stacked method is used for make a graph in type of ratio format like one upon another
data.plot.barh(stacked=True) #barh method is used to make horizontal graph
data.plot.area() #area method is used to get the area graph

#comparing multiple items throgh bar graph

data_analytics = pd.DataFrame({"Total production":[540,485,435,417,456,428,502],
                                "Actual Sale": data['Sales'],
                                "Average Sale" :[100,100,100,100,100,100,100]})

data_analytics.plot.bar()