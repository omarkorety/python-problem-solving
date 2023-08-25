def remove_evens_inplace(lst):
    if lst==0:
        return None
    for i in lst:
        if i % 2 == 0 :
            lst.remove(i) 

    return lst


            










def main():
    lst=list(map(int,input().split()))
    print(remove_evens_inplace(lst))



main()