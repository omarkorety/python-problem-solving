def min_3_vlaues(lst):
    my_lst=[]
    for i in  lst:
        my_lst.append(i)
        if len(my_lst)>3:
            my_lst.sort()
            my_lst.pop()


    my_lst.sort()
    return my_lst    




def main():
    lst=list(map(int,input().split()))
    print(min_3_vlaues(lst))
    
main()