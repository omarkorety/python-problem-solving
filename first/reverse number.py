num=int(input())
number=0
while num>0:
    last_digit= num % 10
    num //=10
    number=number *10 + last_digit
print(number,number*3)




