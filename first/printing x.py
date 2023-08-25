N=int(input())
if N % 2 ==1:
    for i in range(N):
        for j in range(N):
            if i==j or j==N-1-i:
                print("*",end='')
            else:
                print(" ",end='')
        print()

