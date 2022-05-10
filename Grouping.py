string=input()
lst=[]
start_idx=0
for idx in range(1, len(string)):
    if string[idx].lower() !=string[idx-1].lower():
        lst.append(string[start_idx : idx])
        start_idx = idx









print(','.join(lst))
                 