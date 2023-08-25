num_test_cases=int(input())
while num_test_cases > 0:
    num_of_integer=int(input())
    pos =0
    result=0
    while pos < num_of_integer:
        num=int(input())

        if pos==0:
            result=num
        elif result>num:
             result=num
        pos +=1
    print("min value is:",result)
    num_test_cases -= num_test_cases   
