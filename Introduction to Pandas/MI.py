import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('MI.csv',sep=',')															#Importing the .csv for data analysis
print (df.head())																			#Prints first 5 rows
print ("--------------------------------------------------------------------------")
print (df.shape)																			#Dimensions of the data
print (df.columns.values)																	#Names of columns in the data
print (df.info())																			#Describes data types of each column
print ("--------------------------------------------------------------------------")
print (df.describe())																		#Gives statitics of the data
print ("--------------------------------------------------------------------------")
print (df.hist('Rohit'))																	#Creates Histogram																	
print ((df['Rohit']).apply(lambda r: r > 20))												#Boolean Function 
print ("--------------------------------------------------------------------------")
x = ((df['Rohit']).apply(lambda r: r > 40))
y = ((df['Total']).apply(lambda r: r > 150))
print (x & y)																				#And Operator on Boolean Function
print ("--------------------------------------------------------------------------")
df.reindex(np.random.permutation(df.index))													#Shuffle
print (df)
print ("--------------------------------------------------------------------------")
print (df.reindex([0, 14, 15, 1, 2, 16, 9]))												#Printing Rows 
print ("--------------------------------------------------------------------------")



""" Analysis Data """

print(df["Result"].value_counts())
#	print (df.target_names)
print ("--------------------------------------------------------------------------")
g = df.groupby(['Result'])																	#Grouping the data
for key,df_key in g:
	print (key)
	print (df_key)
print ("--------------------------------------------------------------------------")
print (df.groupby(['Result']).describe())
print ("--------------------------------------------------------------------------")
Selected_Players = df[["Rohit","Quinton","Surya","Krunal","Pollard","Hardik"]]
Key_Data = Selected_Players.copy()
print (Key_Data.describe())
print ("--------------------------------------------------------------------------")



plt.figure(figsize=(6,4))
sns.heatmap(df.corr(),cmap='YlGnBu',annot=True)												#Creates the heat map


l = df.columns.values
number_of_columns=10
number_of_rows = len(l)-1/number_of_columns
plt.figure(figsize=((number_of_columns),5*number_of_rows))
for i in range(0,len(l)):
    plt.subplot((number_of_rows + 1),(number_of_columns),i+1)
    sns.set_style('whitegrid')
    sns.boxplot(df[l[i]],color='yellow',orient='v')
    plt.tight_layout()																		#Creates Box plot
    
    

plt.figure(figsize=(2*number_of_columns,5*number_of_rows))
for i in range(0,len(l)):
    plt.subplot(number_of_rows + 1,number_of_columns,i+1)
    sns.distplot(df[l[i]],kde=True)															#Creates Subplot

plt.show()


sns.pairplot(Key_Data, diag_kind='hist')
plt.show()
