N,A,B=map(int,input().split())
total=0
for j in range(1,N+1):

        last_digit=j % 10 #get the last digit
        k=j //10 #remove last digit from i
        sum=last_digit+k
        if A<=sum<=B:
            total +=j

print(total)





