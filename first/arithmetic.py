x,y =map(int,input().split())
if x % 2==1 and y % 2==1:
    print(x*y)
elif x% 2==0 and y % 2==0:
    print(x/y)
elif x% 2==1 and y % 2==0:
    print(x+y)
else:
    print(x-y)