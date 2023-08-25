def is_sequ(lst1,lst2):
    if len(lst2)==0:
        return True

    for item in lst1:
        if item==lst2[0]:
            lst2.pop(0)       #remove the item if it there in list 1 and 2
    return len(lst2)==0

def main():
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    print(is_sequ(lst1,lst2))
main()

