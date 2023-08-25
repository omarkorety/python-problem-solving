from textwrap import indent


lst=list(map(int,input().split()))
temp=[]
for indx,item in enumerate(lst):
    if indx==0 or lst[indx] !=lst[indx-1]:
        temp.append(item)
print(temp)
        