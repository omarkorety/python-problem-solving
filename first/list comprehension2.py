x=int(input())
m=x if x % 2 == 0 else 2 * x
print(m)

lst1=[1,2,3,-4,5,-6,7,8]
lst2= [n if n>0 else -n for n in lst1 if n % 2 == 0]
print(lst2)