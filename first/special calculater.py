while True:
    print("Menu:")
    print("Enter 1 to sum numbers fom 1 to N")
    print("Enter e to evaluate simple numbers expression")
    print("Enter 3 to end the program")
    print()
    num=int(input("Enter choice from 1 to 3 :"))
    if num==1:
        N=int(input("Enter a number :"))
        sum=0
        counter=1
        while counter<N:
            sum +=counter
            counter +=1
        print(sum)
    elif num == 2 :
        num1,operation,num2=input("Enter simple expression").split()
        num1,num2=float(num1),float(num2)
        result=0
        if operation == '+':
            result=num1+num2
        elif operation == '-':
            result=num1-num2
        elif operation == '*':
            result=num1*num2
        elif operation == '**':
            result=num1**num2
        else:
            if num2==0:
                print("error")
            else:
                if operation == "/":
                    result=num1/num2
                elif operation == "//":
                    result=num1//num2
        if result != None:
            print("expression value is",result)
        
    else:
        break


