import numpy as np
def row_panelty(arr,x,y):
    war=np.sort(arr,axis = 1)
    
    row_p = []
    for i in range(x):
        try:
            q = war[i][1]-war[i][0]
        except:
            q = war[i][0]
        row_p.append(q)
    return row_p

def col_panelty(arr,x,y):
    war=np.sort(arr,axis = 0)
    col_p = []
    for i in range(y):
        try:
            x = war[1][i]-war[0][i]
        except:
            x = war[0][i]
        col_p.append(x)
    return col_p
rowp=[]
colp=[]
total = 0
arr = np.array([[1,2,1,4],[3,3,2,1],[4,2,5,9]])
sup = [30,50,20]
dem = [20,40,30,10]
m,n = arr.shape
while(m>0 and n>0):
    
    rowp = row_panelty(arr,m,n)
    colp = col_panelty(arr,m,n)
    maxpen=max(max(rowp),max(colp))
    minval = 1000
    if maxpen in rowp:
        if(rowp.index(maxpen)>=0):
            f,l = [rowp.index(maxpen),0]
            for i in range(n):
                if(arr[f][i]<minval):
                    minval = arr[f][i]   
    elif maxpen in colp: 
        if(colp.index(maxpen)>=0):
            f,l = [0,colp.index(maxpen)]
            for i in range(m):
                if(arr[i][l]<minval):
                    minval = arr[i][l]   
    print(minval)
    for i in range(f,m):
        for j in range(l,n):
            if(arr[i][j]==minval):
                q,w = i,j
                break
    
    mi = minval
    if(dem[w]>sup[q]):
        total = mi*sup[q] + total
        dem[w] = dem[w]-sup[q]
        del(sup[q])
        arr = np.delete(arr,q,axis=0)
        m = m-1
    elif(dem[w]==sup[q]):
        total = mi*sup[q] + total
        del(dem[w])
        del(sup[q])
        arr = np.delete(arr,q,axis=0)
        m = m-1
        
    elif(dem[w]<sup[q]):
        total = mi*dem[w] + total
        sup[q] = sup[q]-dem[w]
        del(dem[w])
        arr = np.delete(arr,w,axis=1)
        n = n-1
    print(total)
    print(arr)    
print(total)    
