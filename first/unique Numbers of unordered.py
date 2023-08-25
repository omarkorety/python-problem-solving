lst=list(map(int,input().split()))
temp=[]
for i in lst:
    if i not in temp:
        temp.append(i)

print(temp)
        