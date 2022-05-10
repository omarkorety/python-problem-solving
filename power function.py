x,y = map(int,input().split())
counter=1
res=1
while counter<=y:
    res=res*x
    counter +=1
print(res)