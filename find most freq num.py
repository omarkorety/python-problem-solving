def repet(lst):
    counter=0
    num=lst[0]
    for i in lst:
        curr_frequ=lst.count(i)
        if curr_frequ> counter:
            counter=curr_frequ
            num=i

        elif curr_frequ==counter:
            num=min(num,i)
            

    return num, counter


def main():
    lst=list(map(int,input().split()))
    print(repet(lst))

main()
        