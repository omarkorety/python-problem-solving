nums=int(input())
counter=1
oddsum=0
evensum=0
even=0
odd=0
while counter<=nums:
    num=float(input())
    if counter % 2 == 1:
        oddsum += num
        odd += 1
    else:
        evensum += num
        even += 1
    counter += 1

print(oddsum/odd,evensum/even)
