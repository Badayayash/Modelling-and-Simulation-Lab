import numpy as np
total = 0
arr = np.array([[19,30,50,10],[70,30,40,60],[40,8,70,20]])
s = [5,8,7,14]
d = [7,9,18]
m,n = arr.shape
print(arr)
while(m>1 or n>1):
    minval = 1000
    for i in range(m):
        for j in range(n):
            if(arr[i][j]<minval):
                minval = arr[i][j]
                x,y = i,j
    print("Min value:")
    print(minval)
    if(d[x]<s[y]):
    	total = total + minval*d[x]
    	s[y] = s[y]-d[x]
    	d[x] = 0
    	arr = np.delete(arr,x,axis =0)
    	del d[x]
    	m = m-1
    elif(d[x]==s[y]):
    	total = total + minval*d[x]
    	s[y] = 0
    	d[x] = 0
    	arr = np.delete(arr,x,axis =0)
    	del d[x]
    	m = m-1
    elif(d[x]>s[y]):
    	total = total + minval*s[y]
    	d[x] = d[x]-s[y]
    	s[y] = 0
    	arr = np.delete(arr,y,axis =1)
    	del s[y]
    	n = n-1
    print("array:")
    print(arr)
    print("total:")
    print(total)
print("Min value:")
print(min(arr[0]))
if(d<s):
	total = total + arr[0]*d[0]
else:
	total = total + arr[0]*s[0]
print("final total:")
print(*total)