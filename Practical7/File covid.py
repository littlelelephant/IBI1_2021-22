import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#use the module

os.chdir('/Users/OMEN/IBI1_2021-22/Practical7')#move to the working directory
print(os.getcwd())#check the working directory
print(os.listdir())# list the file in the directory
covid_data=pd.read_csv("full_data.csv")#give "covid_data" definition
print(covid_data.head(5))#show the first 5 rows of the covid_data
print(covid_data.info())#show the information of the covid_data
print(covid_data.describe())#describe the covid_data
print(covid_data.iloc[0,1])
print(covid_data.iloc[2,0:5])
print(covid_data.iloc[0:2,:])
print(covid_data.iloc[0:10:2,0:5])
print(covid_data.iloc[0:3,[0,1,3]])
my_columns=[True,True,False,True,False,False]
covid_data.iloc[0:3,my_columns]
covid_data.loc[2:4,"date"]
print(covid_data.iloc[9:20,[0,2]])

print(covid_data.loc[0:81,"total_cases"])

Afghanistan_data=[]
for a in range(0,7996):
    if covid_data.iloc[a,1]=="Afghanistan":
        Afghanistan_data.append(True)
    else:
        Afghanistan_data.append(False)
print(covid_data.loc[Afghanistan_data,"total_cases"])#use loop and Boolean to find the total cases of Afghanistan

print(covid_data[covid_data['location']=='Afghanistan']['total_cases'])#another way to show the total cases of Afghanistan

China_data=[]
for c in range(0,7996):
    if covid_data.iloc[c,1]=="China":
        China_data.append(True)
    else:
        China_data.append(False)
china_new_data=covid_data.iloc[China_data,[0,2,3]]
print(china_new_data)
print(china_new_data.describe())
#from the information we found the mean of new cases is 893.92, the mean of deaths is 35.97
China_new_cases=china_new_data.iloc[:,1]
China_new_deaths=china_new_data.iloc[:,2]
China_date=china_new_data.iloc[:,0]

plt.boxplot(China_new_cases,vert=False)#make the boxplot of China new cases
plt.title('China new cases')
plt.show()

plt.boxplot(China_new_deaths,vert=False)#make the boxplot of China new deaths
plt.title('China new deaths')
plt.show()

plt.plot(China_date,China_new_cases,'r+')#'r+'means the color of the note is red and the shape of the note is +
plt.title('China new cases per day')
plt.xticks(China_date.iloc[0:len(China_date):4],rotation=-90)
plt.show()

plt.plot(China_date,China_new_cases,color='red')
plt.plot(China_date,China_new_deaths,color='blue')
plt.title('China daily new cases and new deaths')
plt.xticks(China_date.iloc[0:len(China_date):4],rotation=-90)
plt.xlabel('Date')
plt.ylabel('Amount')
plt.show()

#Q: How have new cases and total cases developover time in Spain?
Spain_data=[]
for s in range(0,7996):
    if covid_data.iloc[s,1]=="Spain":
        Spain_data.append(True)
    else:
        Spain_data.append(False)
Spain_data=covid_data.iloc[Spain_data,:]
Spain_new_cases =Spain_data.iloc[:,2]
Spain_total_cases =Spain_data.iloc[:,4]
Spain_date=Spain_data.iloc[:,0]

plt.plot(Spain_date,Spain_new_cases,color='blue')
plt.plot(Spain_date,Spain_total_cases,color='red')
plt.title("Spain daily new cases and total cases")
plt.xticks(Spain_date.iloc[0:len(Spain_date):4],rotation=-90)
plt.xlabel('Date')
plt.ylabel('Amount')
plt.show()
    






