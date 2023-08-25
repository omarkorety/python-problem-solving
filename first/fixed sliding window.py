def sliding(lst,N):
    max_sum , start_indx = None, None
    for j in range(len(lst)-N+1):
        new_sum=sum(lst[j:N+1])

        if max_sum is None or max_sum < new_sum:
            max_sum,start_indx=new_sum,j

    return j, max_sum
            






if __name__ == '__main__':
    lst=list(map(int,input().split()))
    N=int(input())
    print(sliding(lst,N))



  