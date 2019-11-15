# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 08:33:59 2018

@author: logistica
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
plt.style.use('ggplot')
from sklearn.cluster import KMeans

def deleteInvalids(df):
    deletes=[]
    for i in range(0,len(df[:,0])):
        result=0
        for j in range(0,len(df[i,:])):
            result+=df[i,j]
        if result<=0:
            deletes.append(i)
    df=np.delete(df,deletes,0)
    return df

def printInvalids(df):
    deletes=[]
    for i in range(0,len(df[:,0])):
        result=0
        for j in range(0,len(df[i,:])):
            result+=df[i,j]
        if result<=0:
            deletes.append(i)
    df=np.delete(df,deletes,0)
    return deletes

def normalizeData(df):
    df=np.array(df,dtype=float)
    for i in range(0,len(df[:,0])):
        maxRow=np.amax(df[i,:])
        minRow=np.amin(df[i,:])
        for j in range(0,len(df[i,:])):
            if maxRow==0:
                newValue=0
            else:
                newValue=(df[i,j]-minRow)/(maxRow-minRow)
            df[i,j]=newValue
    return df

def xAxis(df):
    x=[]
    for i in range(0,len(df[0,:])):
        x.append(i)
    return x

def plotSamples(x,df):
    plt.figure(figsize=(20,10))
    plt.xlabel('Día')
    plt.ylabel('Venta')
    for i in range(0,len(df[:,0])):
        plt.plot(x,df[i,:])
    plt.show()

def plotCluster(indexes,n_cluster,df,x):
    plt.figure(figsize=(15,10))
    plt.xlabel('Día')
    plt.ylabel('Venta')
    for i in range(0,len(df[:,0])):
        if indexes[i]==n_cluster-1:
            plt.plot(x,df[i,:])
    plt.show()

'''
# January
january=pd.read_csv('Enero_clustering.csv',sep=';')
january2=january.iloc[:,1:].values
january2=deleteInvalids(january2)
january3=normalizeData(january2)
xJanuary=xAxis(january3)
kmeansJanuary=KMeans(n_clusters=10,random_state=0).fit(january3)
clustersIndexJanuary=kmeansJanuary.labels_
plotCluster(clustersIndexJanuary,10,january3,xJanuary)

# February
february=pd.read_csv('Febrero_clustering.csv',sep=';')
february2=february.iloc[:,1:].values
february2=deleteInvalids(february2)
february3=normalizeData(february2)
xFebruary=xAxis(february3)
kmeansFebruary=KMeans(n_clusters=10,random_state=0).fit(february3)
clustersIndexFebruary=kmeansFebruary.labels_
plotCluster(clustersIndexFebruary,10,february3,xFebruary)

# March
march=pd.read_csv('Marzo_clustering.csv',sep=';')
march2=march.iloc[:,1:].values
march2=deleteInvalids(march2)
march3=normalizeData(march2)
xMarch=xAxis(march3)
kmeansMarch=KMeans(n_clusters=10,random_state=0).fit(march3)
clustersIndexMarch=kmeansMarch.labels_
plotCluster(clustersIndexMarch,10,march3,xMarch)

# April
april=pd.read_csv('Abril_clustering.csv', sep=';')
april2=april.iloc[:,1:].values
april2=deleteInvalids(april2)
april3=normalizeData(april2)
xApril=xAxis(april3)
kmeansApril=KMeans(n_clusters=10, random_state=0).fit(april3)
clustersIndexApril=kmeansApril.labels_       
plotCluster(clustersIndexApril,10,april3,xApril)

# May
may=pd.read_csv('Mayo_clustering.csv', sep=';')
may2=may.iloc[:,1:].values
may2=deleteInvalids(may2)
may3=normalizeData(may2)
xMay=xAxis(may3)
kmeansMay=KMeans(n_clusters=5, random_state=0).fit(may3)
clustersIndexMay=kmeansMay.labels_       
plotCluster(clustersIndexMay,5,may3,xMay)

# June
june=pd.read_csv('Junio_clustering.csv', sep=';')
june2=june.iloc[:,1:].values
june2=deleteInvalids(june2)
june3=normalizeData(june2)
xJune=xAxis(june3)
kmeansJune=KMeans(n_clusters=5, random_state=0).fit(june3)
clustersIndexJune=kmeansJune.labels_       
plotCluster(clustersIndexJune,5,june3,xJune)'''

def plotMonthsClusters(Months, clusters):
    fig = plt.figure(figsize=(70,50))
    #fig.subplots_adjust(hspace=0.2, wspace=0.2)
    i=1
    for j in range(0,len(Months)):
        month=pd.read_csv(Months[j]+'_clustering.csv',sep=';')
        month2=month.iloc[:,1:].values
        month2=deleteInvalids(month2)
        month3=normalizeData(month2)
        xMonth=xAxis(month3)
        kmeansMonth=KMeans(n_clusters=clusters,random_state=0).fit(month3)
        clustersIndexMonth=kmeansMonth.labels_
        for k in range(1,clusters+1):
            ax = fig.add_subplot(len(Months), clusters, i)
            for l in range(0,len(month3[:,0])):
                if clustersIndexMonth[l]==k-1:
                    ax.plot(xMonth,month3[l,:])
            i+=1

Months=['Enero','Febrero','Marzo','Abril','Mayo','Junio']

plotMonthsClusters(Months,6)

#a=pd.read_csv('Junio_clustering.csv', sep=';')
#a2=a.iloc[:,1:].values
#b=printInvalids(a2)
                    
            
            
        
    
    
    
    
    
    
    