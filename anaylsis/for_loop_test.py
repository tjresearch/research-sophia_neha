arr = [0,1,2,3,4,5,6,7]
arr = [(arr[i],arr[i+1]) for i in range(0,len(arr),2)]
for p in arr:
	print(p)
   
filepath = "../output/video_output/VID_TEST_CASE_1_keypoints/VID_TEST_CASE_1_{0:012d}_keypoints.json"
json_frame = open(filepath.format(123), 'r')
print(json_frame)
