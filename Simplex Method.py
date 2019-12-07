def newval(oldval,corcol,corrow,keyele):
	value = oldval - ((corrow*corcol)/keyele)
	return value
iti = 1
print("***Program Begins***")
cost = [-6,-7,-1,0,-12],[-8,-12,0,-1,-20]
cb = [0,0]
cj = [100,120,0,0] 
zj = [0,0,0,0]
czj = [0,0,0,0]
ratio = [0,0]
count = 0
sol = [100,120]
while(count==0):
	for i in range(4):
		x = 0
		for j in range(2):
			x = cb[j]*cost[j][i] + x
		zj[i] = x		
	for i in range(4):
		czj[i] = zj[i]-cj[i]	
	for i in range(4):
		if(czj[i]>=0):
			count = count +1

	if(count == 4):
		break
	count = 0	
	maxval = min(czj)
	colind = czj.index(maxval)
	for i in range(2):
		if(cost[i][colind]!=0):
			ratio[i] = cost[i][4]/cost[i][colind]
	minval = min(ratio)
	rowind = ratio.index(minval)
	keyele = cost[rowind][colind]
	if(rowind ==0):
		corcol = cost[1][colind]
	else:
		corcol = cost[0][colind]
	for i in range(5):
		if(rowind==0):
			cost[1][i] = newval(cost[1][i],corcol,cost[0][i],keyele)
		else:
			cost[0][i] = newval(cost[0][i],corcol,cost[1][i],keyele)	
	for i in range(5):
		cost[rowind][i] = cost[rowind][i]/keyele
	cb[rowind] = cj[colind]	
	sol[0] = cost[0][4]
	sol[1] = cost[1][4]

	print("Cost Matrix at iteration "+str(iti)+" : ",cost)
	print(sol)
	iti = iti +1
print("Values for x1 and y1:","%.2f" %(sol[0]),"%.2f" % (sol[1]))
optsol = cb[0]*cost[0][4]+cb[1]*cost[1][4]
print("Optimal solution for this minimisation problem is:",int(optsol))
print("***Program ended***")