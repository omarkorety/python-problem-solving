N=int(input())
counter=0
nums=0

while counter < N:
    if nums% 3 == 0 and nums% 4 !=0 :
        print(nums)
        counter +=1
    nums +=1

