# 
# Sophia Wang 
# December 5, 2019
# keypoints_parse_12-5-19a.py
# 

import sys
import json
import math 

points_key = {	 '0':	"Nose",  
		 '1':  	"Neck", 
		 '2':  	"RShoulder", 
		 '3':  	"RElbow", 
		 '4':  	"RWrist", 
		 '5':  	"LShoulder",
		 '6':  	"LElbow",
		 '7':  	"LWrist",
		 '8':  	"MidHip",
		 '9':  	"RHip",
		'10': 	"RKnee",
		'11': 	"RAnkle",
		'12': 	"LHip",
		'13': 	"LKnee",
		'14': 	"LAnkle",
		'15': 	"REye",
		'16': 	"LEye",
		'17': 	"REar",
		'18': 	"LEar",
		'19': 	"LBigToe",
		'20':	"LSmallToe",
		'21': 	"LHeel",
		'22': 	"RBigToe",
		'23': 	"RSmallToe",
		'24': 	"RHeel"}
body_points = { "Nose" 		: [],
		"Neck" 		: [],
		"RShoulder" 	: [],
		"RElbow"	: [], 
		"RWrist"	: [], 
		"LShoulder"	: [],
		"LElbow"	: [],
		"LWrist"	: [],
		"MidHip"	: [],
		"RHip"		: [],
		"RKnee"		: [],
		"RAnkle"	: [],
		"LHip"		: [],
		"LKnee"		: [],
		"LAnkle"	: [],
		"REye"		: [],
		"LEye"		: [],
		"REar"		: [],
		"LEar"		: [],
		"LBigToe"	: [],
		"LSmallToe"	: [],
		"LHeel"		: [],
		"RBigToe"	: [],
		"RSmallToe"	: [],
		"RHeel"		: []}

def angle_calc(x1, y1,  x2, y2, x3, y3): # x2, y2 is center point

	jx12 = (x1-x2)
	jy12 = (y1-y2)
	jx32 = (x3-x2)
	jy32 = (y3-y2)

	r12 = math.sqrt(jx12*jx12 + jy12*jy12)
	r32 = math.sqrt(jx32*jx32 + jy32*jy32)
	
	theta = math.acos( (jx12 * jx32 + jy12 * jy32) / (r12*r32) )	
	return math.degrees(theta)	

def frame_parse(frame_num):
	json_frame = open("../output/video_output/VID_TEST_CASE_1_keypoints/VID_TEST_CASE_1_{0:012d}_keypoints.json".format(frame_num), 'r')
    	data = json_frame.read()

	frame = json.loads( data )  
	for k in frame:
	    print(k)        
	    if k == "version": 
		continue
	    temp = frame[k]
	    print()
	    for i in temp: 
		for j in i: 
		    if j in points_key:
			print(j,points_key[j], i[j])
			body_points[j].append((i[j][0], i[k][1]))
		    else:
			print(j, i[j])
	 
	return  

print(angle_calc(1,0,0,0,0,1))
i = 234
with open("../output/video_output/VID_TEST_CASE_1_keypoints/VID_TEST_CASE_1_{0:012d}_keypoints.json".format(i), 'r') as tfile: 
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
