def nth_fib(n):
    if  n ==1:
        return 0
    if n== 2:
        return 1

    a,b=0,1
    n -=2

    while n>0:
        c=a+b
        a=b
        b=c
        n -=1
    return c

       
for i in range(1,10):
    print(i,nth_fib(i))