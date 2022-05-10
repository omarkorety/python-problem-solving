def is_increasing(lst):
    for i in range(len(lst)):

        if lst[i+1]>=lst[i]:
            return True
        return False
def main():
    lst=list(map(int,input().split()))
    print(is_increasing(lst))

main()

        
