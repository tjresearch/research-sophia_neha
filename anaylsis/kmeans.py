#
# Neha Bagalkot
# January 10, 2020
# kmeans.py
#

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

data = []

for i in range(1, 5):
    filepath = "../output/output_angle_calc/VID_TEST_CASE_{0:}_angles.txt".format(i)
    '''f = open(filepath, 'r')
    print(f.readline().strip())'''
    with open(filepath) as f:
        for line in f:
            data.append(list(line.strip()))

wcss = []
for i in range(1, 21): #trying out different numbers of clusters
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_) #inertia_ tells you how good it is

kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0) #picking the optimum # of clusters
pred_y = kmeans.fit_predict(data)
print(kmeans.cluster_centers_) #should give the coordinates of the centers