import numpy as np
main = [[80,40,50,46],[40,70,20,25],[30,10,20,30],[35,20,25,30]]
mat = np.array([[80,40,50,46],[40,70,20,25],[30,10,20,30],[35,20,25,30]])
row_min = np.amin(mat,axis = 1)
new = []
#row reduction
for i in range(4):
	for j in range(4):
		mat[i][j] = mat[i][j] - row_min[i]
#column reduction
col_min = np.amin(mat,axis = 0)
for i in range(4):
	for j in range(4):
		mat[j][i] = mat[j][i] - col_min[i]
mid_mat = np.array(mat)		
#reduction Completed
loop_v = 0

#loop begins
while(loop_v !=4):
	list1 = []
	list1.clear
	loop_v = 0
	print(mat)
	for i in range(4):
		count = 0
		
		for j in range(4):
			if(mat[i][j]==0):
				count = count +1
				q = j
		if(count == 1):
			loop_v = loop_v + 1
			x = (i,q)
			list1.append(x)
			for p in range(4):
				mat[p][q] = 9999 

	for i in range(4):
		count  =0
		for j in range(4):
			if(mat[j][i]==0):
				count = count +1
				q = j
		if(count == 1):
			loop_v = loop_v + 1
			x = q,i
			list1.append(x)
			
			for p in range(4):
				if(mat[q][p]!=9999):
					mat[q][p] = 9999
				else:
					mat[q][p] = 8888				
	if(loop_v==4):
		break
					
	print(mat)				
	mat_min = np.amin(mat)
	for i in range(4):
		for j in range(4):
			if(mat[i][j]!=9999 and mat[i][j]!=8888):
				mat[i][j] = mat[i][j] - mat_min
			if(mat[i][j]==8888):
				mat[i][j] = mid_mat[i][j]
				mat[i][j] = mat[i][j] + mat_min
			if(mat[i][j]==9999):
				mat[i][j] = mid_mat[i][j]
			
#output
final = 0

print("minimum values:")
for i in range(len(list1)):
	x,y = list1[i][0],list1[i][1]
	final = main[x][y] + final
	print(main[x][y])
print("final minimum cost:",final)