#
# Sophia Wang
# December 10, 2019
# keypoints_parse_12-10-19b.py
#

import sys, os
import json
import math

body_angle_key = {0: (1, 0, 15),  # -------
                1: (1, 0, 16),  # /       \
                2: (0, 1, 2),  # |	  o o   |
                3: (1, 2, 3),  # \   O   /
                4: (2, 3, 4),  # -------
                5: (0, 1, 5),  # | |
                6: (1, 5, 6),  #
                7: (5, 6, 7),  #
                8: (0, 1, 8),  #
                9: (2, 1, 8),
                10: (5, 1, 8),
                11: (1, 8, 9),
                12: (8, 9, 10),
                13: (9, 10, 11),
                14: (10, 11, 24),
                15: (10, 11, 22),
                16: (1, 8, 12),
                17: (8, 12, 13),
                18: (12, 13, 14),
                19: (13, 14, 21),
                20: (13, 14, 19),
                21: (5, 1, 2),     # NEW ANGLES
                22: (7, 8, 4),
                23: (14, 8, 11),
                24: (1, 8, 7),
                25: (1, 5, 4)}

hand_angle_key = {0: (0, 1, 2),  # \ | | | | /
                  1: (1, 2, 3),  # \||||
                  2: (2, 3, 4),
                  3: (0, 5, 6),
                  4: (5, 6, 7),    #      |   |  |   |
                  5: (6, 7, 8),    #       |  |  |  |
                  6: (0, 9, 10),   #        | |  |  |
                  7: (9, 10, 11),  #          |  |  |
                  8: (10, 11, 12), #     |    |||||||
                  9: (0, 13, 14),  #      |   |||||||
                  10: (13, 14, 15),#       ||||||||||
                  11: (14, 15, 16),
                  12: (0, 17, 18),
                  13: (17, 18, 19),
                  14: (18, 19, 20)}

hand_angle_key_cont = {21: (0, 1, 2),
                       22: (1, 2, 3),
                       23: (2, 3, 4),
                       24: (0, 5, 6),
                       25: (5, 6, 7),
                       26: (6, 7, 8),
                       27: (0, 9, 10),
                       28: (9, 10, 11),
                       29: (10, 11, 12),
                       30: (0, 13, 14),
                       31: (13, 14, 15),
                       32: (14, 15, 16),
                       33: (0, 17, 18),
                       34: (17, 18, 19),
                       35: (18, 19, 20)}

points_key = {	'0':	"Nose",
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

frame_angle = {}  # int frame number : [angles]

def angle_calc(x1, y1,  x2, y2, x3, y3): # x2, y2 is center point

    jx12 = (x1 -x2)
    jy12 = (y1 -y2)
    jx32 = (x3 -x2)
    jy32 = (y3 -y2)

    r12 = math.sqrt(jx12 *jx12 + jy12 *jy12)
    r32 = math.sqrt(jx32 *jx32 + jy32 *jy32)

    if (r12 * r32) == 0: #in case the keypoints were just 0
        return 0

    theta = math.acos( (jx12 * jx32 + jy12 * jy32) / (r12 *r32) )
    return math.degrees(theta)

def body_frames(): # NOT TESTED - to go through all the files and collect and write the data
                    #you'll have to change the path names
    # i made a folder called output_angle_calc to write the outputs in - that's commpath0
    commpath0 = r'C:\Users\1707612\PycharmProjects\SeniorResearch\research-sophia_neha-master\research-sophia_neha-master\output' + r'\output_angle_calc'
    commpath = r'C:\Users\1707612\PycharmProjects\SeniorResearch\research-sophia_neha-master\research-sophia_neha-master\output\output_motion_test'

    for d1 in os.listdir(commpath):
        savepath = commpath0 + '\\' + d1 + '.txt' # making filename to write it to
        f = open(savepath, 'x') # making a file for every vid test case to write the frame angles to - rn should be just a bunch of lists
        for filename in os.listdir(commpath + '\\' + d1):
            if filename.endswith(".json"):
                # print(os.path.join(directory, filename))
                output = frame_parse(commpath + '\\' + d1 + '\\' + filename)
                f.write(output)
            else:
                continue
    return

def frame_parse(frame_num): # takes an int, corresponding to the number on the file name, {0:012d} formats num with 0's in front 
    json_frame = open("../output/video_output/VID_TEST_CASE_1_keypoints/VID_TEST_CASE_1_{0:012d}_keypoints.json".format(frame_num), 'r')
    data = json_frame.read()
    frame = json.loads( data )
        
    frame_angles = [] 		    # the list to store all angles for the frame - should probs convert to dict
    people = frame["people"] 	# pose points, l/r hand points, face points (2d and 3d)
    for keys in people:		    # keyval: people -> hand,face keypoints etc. part_candidates->candidates for
        print(keys)
        for key in keys:
            if(key == "person_id"):
                continue
            print(key)
            if key == 'pose_keypoints_2d':	#to do only the first pose keypoints set. idk which one to do
                keypoints = keys[key]
                grouped = [(keypoints[i], keypoints[ i +1]) for i in range(0 ,len(keypoints) ,3)]
                '''for g in grouped:
                    print(g)'''
                for angval in body_angle_key: #to calculate all angles in frame
                    v = body_angle_key[angval]
                    ang = angle_calc(grouped[v[0]][0], grouped[v[0]][1], \
					                 grouped[v[1]][0], grouped[v[1]][1], \
                                     grouped[v[2]][0], grouped[v[2]][0])
                    frame_angles.append(ang)
    return frame_angles

print(frame_parse(234));
'''print(angle_calc(1 ,0 ,0 ,0 ,0 ,1))
i = 234
with open("../output/video_output/VID_TEST_CASE_1_keypoints/VID_TEST_CASE_1_{0:012d}_keypoints.json".format(i), 'r') as tfile:
    data = tfile.read()

frame0 = json.loads( data )
print(frame0)
for key_name in frame0:  # key_name = "version", "people", "part_candidates"
    print()
    print(key_name)
    if key_name == "people":
        keyval = frame0[key_name  ]# pose points, l/r hand points, face points (2d and 3d)
        for i in keyval:	 # keyval: people -> hand, face keypoints etc. part_candidates -> candidates for the
            for j in i: 	 # body part before assembling, don't worry about it
                if j in points_key:
                    print(j ,points_key[j], i[j])
                else:
                    print(j, i[j])
frame_parse(234)
'''
'''for key_name in frame0: #key_name = "version", "people", "part_candidates" 
	print(key_name)
	if k == "version": 
		continue
	key_val = frame0[k] # people: person id,  
	print(key_val)
	for i in key_val: # keyval: people -> hand, face keypoints etc. part_candidates -> candidates for the body part before 
		print(i)  # assembling, don't worry about it 
'''
