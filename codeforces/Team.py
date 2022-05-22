nums=int(input())
res=0
for i in range(nums):
    idea=list(map(int,input().split()))
    if idea.count(1) >=2:
        res += 1
    
        
print(res)                                                                                        