#
# Sophia Wang
# December 16, 2019
# keypoints_parse_12-16-19a.py
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
                  21: (5, 1, 2),  # NEW ANGLES
                  22: (7, 8, 4),
                  23: (14, 8, 11),
                  24: (1, 8, 7),
                  25: (1, 5, 4)}

hand_angle_key = {0: (0, 1, 2),  # \ | | | | /
                  1: (1, 2, 3),  # \||||
                  2: (2, 3, 4),
                  3: (0, 5, 6),
                  4: (5, 6, 7),  # |   |  |   |
                  5: (6, 7, 8),  # |  |  |  |
                  6: (0, 9, 10),  # | |  |  |
                  7: (9, 10, 11),  # |  |  |
                  8: (10, 11, 12),  # |    |||||||
                  9: (0, 13, 14),  # |   |||||||
                  10: (13, 14, 15),  # ||||||||||
                  11: (14, 15, 16),
                  12: (0, 17, 18),
                  13: (17, 18, 19),
                  14: (18, 19, 20)}

points_key = {'0': "Nose",
              '1': "Neck",
              '2': "RShoulder",
              '3': "RElbow",
              '4': "RWrist",
              '5': "LShoulder",
              '6': "LElbow",
              '7': "LWrist",
              '8': "MidHip",
              '9': "RHip",
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
              '20': "LSmallToe",
              '21': "LHeel",
              '22': "RBigToe",
              '23': "RSmallToe",
              '24': "RHeel"}
body_points = {"Nose" 	: [],
                "Neck" 		: [],
                "RShoulder" 	: [],
                "RElbo"	: [],
                "RWris"	: [],
                "LShoulde"	: [],
                "LElbo"	: [],
                "LWris"	: [],
                "MidHi"	: [],
                "RHip"		: [],
                "RKnee"		: [],
                "RAnkl"	: [],
                "LHip"		: [],
                "LKnee"		: [],
                "LAnkl"	: [],
                "REye"		: [],
                "LEye"		: [],
                "REar"		: [],
                "LEar"		: [],
                "LBigTo"	: [],
                "LSmallTo"	: [],
                "LHeel"		: [],
                "RBigTo"	: [],
                "RSmallTo"	: [],
                "RHeel"		: []}


# frame_angle = {}  # int frame number : [angles]

def angle_calc(x1, y1, x2, y2, x3, y3)  : # x2, y2 is center point
    jx12 = (x1 - x2)
    jy12 = (y1 - y2)

    jx32 = (x3 - x2)
    jy32 = (y3 - y2)

    r12 = math.sqrt(jx12 * jx12 + jy12 * jy12)
    r32 = math.sqrt(jx32 * jx32 + jy32 * jy32)

    if (r12 * r32) == 0:
        return 0

    cosang = (jx12 * jx32 + jy12 * jy32) / (r12 * r32)
    if cosang > 1 and cosang<1.01:
        cosang = 1

    theta = math.acos(cosang)
    return math.degrees(theta)

def body_frames(output_folder): # output folder = VID_TEST_CASE_# without the keypoints at the end

    outpath = "../output/output_angle_calc/{0:}_angles.txt".format(output_folder)
    inpath  = "../output/video_output/{0:}_keypoints/{0:}_{1:012d}_keypoints.json"
    i = 0
    output = open(outpath, 'w')
    while(os.path.isfile(inpath.format(output_folder, i))): # checks if the input file exists 
        output.write(str(frame_parse(inpath.format(output_folder, i))) + '\n') # writes the angle file 
        i += 1
    output.close()

def frame_parse(filepath):  # takes number on the file name, {0:012d} formats num with 0's in front
    json_frame = open(filepath, 'r')
    print(filepath)
    data = json_frame.read()
    frame = json.loads(data)

    frame_angles = []   # the list to store all angles for the frame - should probs convert to dict
    people = frame["people"]  # pose points, l/r hand points, face points (2d and 3d)
    for keys in people:  # keyval: people -> hand,face keypoints etc. part_candidates->candidates for
        # print(keys)
        for key in keys:
            if (key == "person_id"):
                continue
            #    print(key)
            if key == 'pose_keypoints_2d':  # to do only the first pose keypoints set. idk which one to do
                keypoints = keys[key]
                grouped = [(keypoints[i], keypoints[i + 1]) for i in range(0, len(keypoints), 3)]
                for angval in body_angle_key:  # to calculate all angles in frame
                    v = body_angle_key[angval]
                    ang = angle_calc(grouped[v[0]][0], grouped[v[0]][1],
                                     grouped[v[1]][0], grouped[v[1]][1],
                                     grouped[v[2]][0], grouped[v[2]][1])
                    frame_angles.append(ang)
    return frame_angles


folder = "VID_TEST_CASE_9"
body_frames(folder)

