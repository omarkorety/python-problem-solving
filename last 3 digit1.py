x= int(input())
if x<10000:
    print("this is a small number")
else:
    a= x%10    #get the last digit
    x=x//10    #remove last digit
    b=x%10     #get the last digit
    x=x//10    #remove last digit
    c= x%10    #get the last digit
    sum=a+b+c
    if sum % 2== 1:
        print("this is a great number")
    else:
        if a  % 2== 1 or  b % 2== 1 or b % 2== 1:
            print("this os a good number")
        else:
            print("this is a bad number")