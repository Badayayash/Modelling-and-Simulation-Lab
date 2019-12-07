import numpy as np
arr = np.array([[1,2,1,4],[3,3,2,1],[4,2,5,9]])
d = [30,50,20]
s = [20,40,30,10]
total = 0
m,n = arr.shape
print(arr)


def row_panelty(arr,m,n):
	r = 0
	c = 0
	id = []
	while (r < m):
		first = 1000
		second = 1000
		for c in range(0,n):

			if(arr[r][c] <= first):
				second = first
				first = arr[r][c]

			elif(arr[r][c]<second and arr[r][c]>first):
				second = arr[r][c]

			
		x = second - first
		id.append(x)
		r = r + 1
	return id

def column_panelty(arr,m,n):

	q = 0
	w = 0

	su = []
	while (q < n):
		first = 1000
		second = 1000
		for w in range(0,m):

			if(arr[w][q] <= first):
				second = first
				first = arr[w][q]

			elif(arr[w][q]<second and arr[w][q]>first):
				second = arr[w][q]
				

		
		x = second - first
		su.append(x)
		q = q + 1
	return su

while(m > 0 and n > 0):
	row = row_panelty(arr,m,n)
	column = column_panelty(arr,m,n)
	max_p = max(max(row),max(column))
	f = 0
	l = 0
	if max_p in row:
		if(row.index(max_p)>=0):
			max_i = [row.index(max_p),0]
	elif max_p in column:	
		if(column.index(max_p)>=0):
			max_i = [0,column.index(max_p)]
	
	f,l = max_i

	minval = 100000
	x  = 0
	y = 0
	for i in range(f,m):
	    for j in range(l,n):
	        if(arr[i][j]<minval):
	            minval = arr[i][j]
	            x,y = i,j
	
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
	print(total)
print('Final Total: ')
print(total)