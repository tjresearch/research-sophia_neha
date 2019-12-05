# 
# Sophia Wang 
# December 3, 2019
# keypoints_parse_12-3-19a.py
# 

import sys
import json
points_key = {'0':"Nose",  
        '1': "Neck", 
        '2': "RShoulder", 
        '3':"RElbow", 
        '4': "RWrist", 
        '5': "LShoulder",
        '6':  "LElbow",
        '7':  "LWrist",
        '8': "MidHip",
        '9':  "RHip",
        '10': "RKnee",
        '11': "RAnkle",
        '12': "LHip",
        '13': "LKnee",
        '14': "LAnkle",
        '15': "REye",
        '16': "LEye",
        '17': "REar",
        '18': "LEar",
        '19': "LBigToe",
        '20':"LSmallToe",
        '21': "LHeel",
        '22': "RBigToe",
        '23': "RSmallToe",
        '24': "RHeel",
        '25': "Background"}



with open("../output/output_motion_test/VID_TEST_CASE_1_keypoints/VID_TEST_CASE_1_000000000000_keypoints.json", 'r') as tfile: 
    data = tfile.read()
frame0 = json.loads( data )  
for k in frame0:
    print(k)        
    if k == "version": 
        continue
    temp = frame0[k]
    print()
    for i in temp: 
        for j in i: 
            if j in points_key:
                print(j,points_key[j], i[j])
            else:
                print(j, i[j])
       # for j in temp[i]:
        #    print(j)
