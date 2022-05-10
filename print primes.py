N=int(input())

for i in range(2,N+1):
    is_ok=True
    for j in range(2,i):
        if i % j == 0 :
            is_ok=False
    if is_ok:
        print(i,end='')
            