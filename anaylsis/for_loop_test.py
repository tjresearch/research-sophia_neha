arr = [0,1,2,3,4,5,6,7]
arr = [(arr[i],arr[i+1]) for i in range(0,len(arr),2)]
for p in arr:
	print(p)
