def min_3_vlaues(lst):
    for i in lst:
        if len(lst) > 3:
            lst.sort()
            lst.pop()
        lst.sort()
    return lst


def main():
    lst=list(map(int,input().split()))
    print(min_3_vlaues(lst),end=" ")
main()