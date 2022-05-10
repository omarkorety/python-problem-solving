N=int(input())
lst=[0]*N
for i in range(N):
    name, age,salary = input().split()
    lst[i]=name,int(age),int(salary)


lst.sort()
for idx ,(name,age,salary) in enumerate(lst):
    print(idx,name,age,salary)

    