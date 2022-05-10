def print_menu():
    
    print("Menu:")
    print("Enter 1 to sum numbers fom 1 to N")
    print("Enter e to evaluate simple numbers expression")
    print("Enter 3 to end the program")
    print()
        
### function to sum all numbers from 1 to n number entered by user
def sum_1_to_n():

    N=int(input("Enter a number :"))
    sum=0
    for i in range(1,N+1):
        sum +=i
    print(sum)

### function to division operation
def divide(num1,num2,operation):
    if num2==0:
        result=None
    elif operation == "/":
        result=num1/num2
    else :
        result=num1//num2

    return result


def expression():
    num1,operation,num2=input("Enter simple expression : ").split()
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
        result = divide(num1,num2,operation)
    if result != None:
            print("expression value is",result)
    else:
        print("Sorry No way to compute this expression")
    


def calculator_interface():
    while True:
        print_menu()
        num=int(input("Enter choice from 1 to 3 :"))
        if num==1:
            sum_1_to_n()
        elif num==2:
            expression()
        else:
            break
        




    
calculator_interface()