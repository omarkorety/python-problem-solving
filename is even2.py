n = int(input())
if n % 2 ==0:
    print(n % 10)#print last digit
else:
    if n < 1000:
        print(n % 100)#print last 2 digit
    elif   n < 1000000 :
        print(n %10000)#print last 4 digit
    else:
        print(-n)
