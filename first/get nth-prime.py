def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
            if n % i == 0:
                return False
    return True
def nth_prime(a):
    counter=2
    while a > 0:
        if is_prime(a):
            n -= 1
            if n == 0:
                return counter
        counter +=1
    return -1

            
for i in range(1,10):
    print(i,nth_prime(i))
            

        

         
#didnt work function homeworke