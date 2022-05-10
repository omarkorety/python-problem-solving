n=int(input())
row=1
while row<=n:
    counter=n
    while counter>=row:
        print('*',end='')
        counter -=1
    print()
    row +=1


