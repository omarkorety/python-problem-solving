from calendar import c


N, M , W = map(int,input().split())
total=0

for A in range(1, N+1):
    for B in range(A, M+1):
        for c in range(1,W+1):
            if A+B<=c:
                total +=1
print(total)