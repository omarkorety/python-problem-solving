def dig_freq(lst):
    freq=[0]*10
    for value in lst:
        #convert the num to string and add it
        string=str(abs(value))
        for char in string:
            freq[int(char)] += 1    ##here we used the numbers in the list as index every time it's repeated we increse 1 to thier index
        

    return freq


def main():
    lst=list(map(int,input().split()))
    freq=dig_freq(lst)
    for idx in range(10):
        print(idx,freq[idx])

main()

