#
# Neha Bagalkot
# February 5, 2020
# kmeans_2-5-20.py
#

#import numpy as np
#import pandas as pd
#from matplotlib import pyplot as plt
#from sklearn import cluster
from sklearn.cluster import KMeans

data = []
count = 0

for i in range(1, 5):
    filepath = "../output/output_angle_calc/VID_TEST_CASE_{0:}_angles.txt".format(i)
    f = open(filepath, 'r')
    #print(f.readline().strip())
    with open(filepath) as f:
        for line in f:
            m = line[1:-2]
            oldl = (m.split(', '))
            newl = []
            for j in oldl:
                if len(j)>=1:
                    newl.append(float(j))
            if len(newl) == 26:
                data.append(newl)

wcss = []
finaldata = [data]
print(data)

for i in range(1, 21): #trying out different numbers of clusters
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_) #inertia_ tells you how good it is
print(wcss)

'''kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0) #picking the optimum # of clusters
pred_y = kmeans.fit_predict(data)
print(kmeans.cluster_centers_) #should give the coordinates of the centers'''