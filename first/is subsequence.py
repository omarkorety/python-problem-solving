def is_sequ(lst1,lst2):
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst2[j] in lst1:
                if lst1.index(lst2[j]) < lst1.index(lst2[j+1]):
                    return True 

            return False

def main():
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    print(is_sequ(lst1,lst2))
main()

