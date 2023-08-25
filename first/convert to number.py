import string


def our_int(string):
    res=0
    digits='0123456789'
    for i in string:
        res=res*10 +digits.find(i)
    return print(f'{res} {3*res}')
        
            

def main():
    string=input()
    our_int(string)


main()