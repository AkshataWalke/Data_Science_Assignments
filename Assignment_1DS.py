# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:25:55 2024

@author: Akshata Walke
"""
'''

Problem Statements:
    
Problem Statements:
  1Perform K means clustering on the airlines
 dataset to obtain optimum number of clusters.
 Draw the inferences from the clusters obtained.
 Refer to EastWestAirlines.xlsx dataset
'''
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("C:/cluster_assignment/EastWestAirlines.xlsx")
df

from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
df=pd.read_excel("C:/cluster_assignment/EastWestAirlines.xlsx")
df.head()

plt.scatter(df.Balance,df['Qual_miles'])
plt.xlabel('Balance')
plt.ylabel('Qual_miles')

km=KMeans(n_clusters=3)

y_predicted=km.fit_predict(df[['Balance','Qual_miles']])
y_predicted
df['cluster']=y_predicted

df.head()
km.cluster_centers_

df1= df[df.cluster==0]
df2= df[df.cluster==1]
df3= df[df.cluster==2]

plt.scatter(df1.Balance,df1['Qual_miles'],color='green')
plt.scatter(df2.Balance,df2['Qual_miles'],color='red')
plt.scatter(df3.Balance,df3['Qual_miles'],color='black')


plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.xlabel('Balance')
plt.ylabel('Qual_miles')
plt.legend


#preprocessing using min max scaler

scaler = MinMaxScaler()

scaler.fit(df[['Qual_miles']])
df['Qual_miles']=scaler.transform(df[['Qual_miles']])

scaler.fit(df[['Balance']])
df['Balance']=scaler.transform(df[['Balance']])
df.head()

plt.scatter(df.Balance,df['Qual_miles'])
plt.xlabel('Balance')
plt.ylabel('Qual_miles')

km=KMeans(n_clusters=3)

y_predicted=km.fit_predict(df[['Balance','Qual_miles']])
y_predicted
df['cluster']=y_predicted

df.head()
km.cluster_centers_

################################
df1= df[df.cluster==0]
df2= df[df.cluster==1]
df3= df[df.cluster==2]

plt.scatter(df1.Balance,df1['Qual_miles'],color='green')
plt.scatter(df2.Balance,df2['Qual_miles'],color='red')
plt.scatter(df3.Balance,df3['Qual_miles'],color='black')

plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.xlabel('Balance')
plt.ylabel('Qual_miles')
plt.legend

####################################################################################################################################33

