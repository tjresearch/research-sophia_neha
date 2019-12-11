# 
# Sophia Wang 
# December 9, 2019
# keypoints_parse_12-9-19a.py
# 

import sys
import json
import math 
body_angle_key ={0: ( 1,  0, 15), 
		 1: ( 1,  0, 16),
		 2: ( 0,  1,  2),
		 3: ( 1,  2,  3),
		 4: ( 2,  3,  4),		
		 5: ( 0,  1,  5),
		 6: ( 1,  5,  6),
		 7: ( 5,  6,  7),
		 8: ( 0,  1,  8),
		 9: ( 2,  1,  8),
		10: ( 5,  1,  8),
		11: ( 1,  8,  9),
		12: ( 8,  9, 10),
		13: ( 9, 10, 11),
		14: (10, 11, 24),
		15: (10, 11, 22),
		16: ( 1,  8, 12),
		17: ( 8, 12, 13),
		18: (12, 13, 14),
		19: (13, 14, 21),
		20: (13, 14, 19)}	 

hand_angle_key ={0: ( 0,  1,  2),
		 1: ( 1,  2,  3),
		 2: ( 2,  3,  4),
		 3: ( 0,  5,  6),
		 4: ( 5,  6,  7),
		 5: ( 6,  7,  8), 
		 6: ( 0,  9, 10),
		 7: ( 9, 10, 11),
		 8: (10, 11, 12),
		 9: ( 0, 13, 14),
		10: (13, 14, 15),
		11: (14, 15, 16),
		12: ( 0, 17, 18),
		13: (17, 18, 19),
		14: (18, 19, 20)}


hand_angle_key_cont ={21: ( 0,  1,  2),
		22: ( 1,  2,  3),
		23: ( 2,  3,  4),
		24: ( 0,  5,  6),
		25: ( 5,  6,  7),
		26: ( 6,  7,  8), 
		27: ( 0,  9, 10),
		28: ( 9, 10, 11),
		29: (10, 11, 12),
		30: ( 0, 13, 14),
		31: (13, 14, 15),
		32: (14, 15, 16),
		33: ( 0, 17, 18),
		34: (17, 18, 19),
		35: (18, 19, 20)}

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
frame_angle = {} #int frame number : [angles] 
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
			frame_angle[frame_num] 
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
