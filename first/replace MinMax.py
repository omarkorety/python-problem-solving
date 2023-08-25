#fun to replace min and max values of array
def replace_min_max_inplace(lst):
    min_num=min(lst)
    max_num=max(lst)
    for i in range(len(lst)):
        if lst[i]==min_num:
            lst[i]=max_num
        elif lst[i]==max_num:
            lst[i]=min_num

    
    print(lst)
lst=list(map(int,input().split()))
replace_min_max_inplace(lst)

        
