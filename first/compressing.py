def comprass(str):
    str_len=len(str)
    res="_"
    for i in range(str_len):
        if str_len>0:
            if str[i] !=str[i-1]:
                counter =str.count(str[i])
                print(f"{counter}{str[i]}",end='')
        else:
            print(str[i])




def main():
    string=input()
    comprass(string)




main()
