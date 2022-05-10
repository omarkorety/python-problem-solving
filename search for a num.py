
def searc(lst,query):
    for item in query:
        for index,i in enumerate(lst):
            if item in lst:
                return max(index)





def main():
    lst=list(map(int,input().split()))
    query=list(map(int,input().split()))
    print(searc(lst,query))


main()
