x=int(input())
counter=0
if x==0:
    counter=1
else:
    if x<0:
        x=-x
    while x>0:
        x=x//10
        counter +=1
    
print(counter)
