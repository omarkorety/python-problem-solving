m,k=map(int,input().split())
l=list(map(int,input().split()))
sum=0
for i in l:
    if i <= k:
        sum +=1
    else:
        sum +=2
print(sum)
    