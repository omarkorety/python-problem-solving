steps = 0
mystr = 'hello123uj'
 
for char in mystr:
    if '0' <= char <= '9':
        break
    steps += 1
 
print(steps)