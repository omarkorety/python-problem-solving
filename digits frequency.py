def dig_freq(lst):
        for i in range(10):
            count=lst.count(i)
            print(i,count)


def main():
    lst=list(map(int,input().split()))
    print(dig_freq(lst))

main()