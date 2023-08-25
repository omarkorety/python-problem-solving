N, M , SUM = map(int,input().split())
total=0

for A in range(1, N+1):
    for B in range(1, M+1):
        if A+B==SUM:
            total +=1
print(total)