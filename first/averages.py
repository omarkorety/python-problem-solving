from audioop import avg
from statistics import mean


num1,num2,num3,num4,num5 = map(int,input().split())
print(int((num1+num2+num3+num4+num5)/5))
print((num1+num2+num3)/(num4+num5))
print((num1+num2+num3)/3/((num4+num5)/2))