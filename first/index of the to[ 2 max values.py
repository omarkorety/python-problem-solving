##fun to get  max value

def max_nums(lst):
    return max(lst)
##fun to get index of max value
def get_index(lst):
    if len(lst)==0:
        return None
    return lst.index(max(lst))

def main():
    lst=list(map(int,input().split()))
    for i in range(2):
        print(get_index(lst),max_nums(lst))
        lst.remove(max_nums(lst))


    
    


main()