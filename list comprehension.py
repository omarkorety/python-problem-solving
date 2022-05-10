lst1=[1,-2,6,-3,2,-6]
lst2=[]
lst2=[i*i+1  for i in lst1]
print(lst2)

lst3=[]
lst3=[n+1 for n in range(5,9)]
print(lst3)

lst4=[]
lst3=[3*char for char in 'hey']
print(lst3)

lst5=[]
lst5=[n for n in lst1   if n>0]
print(lst5)


lst6=[]
lst6=[n for n in lst1   if n % 2 ==0]
print(lst6)



lst7=[]
lst7=[n for n in lst1   if n % 2 ==0 and n % 3==0]
print(lst7)

lst8=[]
lst8=[n for n in lst1   if n % 2 ==0 if n % 3==0]
print(lst8)



sentence='Glad that you took this course'
vowels = [i for i in sentence if i in 'aeiou']
print(vowels)
