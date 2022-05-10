def is_sublist(lst1,lst2):
    if len(lst2)==0:
        return True
    lst3=[lst2.pop(0) for item in lst1 if item==lst2[0]]
    return lst3



def main():
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    print(is_sublist(lst1,lst2))
main()

