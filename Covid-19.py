import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('Covid-19.csv',sep=',')												#Importing the .csv for data analysis
print (df.tail())																		#Importing the .csv for data analysis
print ("--------------------------------------------------------------------------")
print (df.shape)																		#Dimensions of the data
print (df.columns.values)																#Names of columns in the data
print (df.info())																		#Describes data types of each column
print ("--------------------------------------------------------------------------")
print (df.describe())																	#Gives statitics of the data
print ("--------------------------------------------------------------------------")

plt.figure(figsize=(6,4))
sns.heatmap(df.corr(),cmap='YlGnBu',annot=True)											#Creates the heat map


l = df.columns.values
number_of_columns=8
number_of_rows = len(l)-1/number_of_columns
plt.figure(figsize=(number_of_columns,5*number_of_rows))
for i in range(0,len(l)):
    plt.subplot(number_of_rows + 1,number_of_columns,i+1)
    sns.set_style('whitegrid')
    sns.boxplot(df[l[i]],color='yellow',orient='v')										#Creates Box plot
    plt.tight_layout()
    
    

plt.figure(figsize=(2*number_of_columns,5*number_of_rows))
for i in range(0,len(l)):
    plt.subplot(number_of_rows + 1,number_of_columns,i+1)
    sns.distplot(df[l[i]],kde=True)														#Creates Subplot

plt.show()
