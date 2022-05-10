num1,num2,num3 = map(int,input().split())
if num3>num1<num2:
    print(num1)
elif num3>num2<num1:
    print(num2)
else:
    print(num3)

