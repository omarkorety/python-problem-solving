def most_freq(lst):
    most_value=0
    frequency=0
    for i in lst:
        curn_freq=lst.count(i)
        if curn_freq > frequency:
            frequency=curn_freq
            most_value=i

        elif curn_freq==most_value:
            most_value=i
    return most_value, frequency






def main():
    lst=list(map(int,input().split()))
    most_value,frequency=most_freq(lst)
    print('value',most_value,"repeated",frequency)
main()
        