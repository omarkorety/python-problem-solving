count=0
for x in range(50,301):
    for y in range(70,401):
        if x<y and (x+y) % 7==0:
            count += 1
           
print(count)
