word= input()
lower_cou=0
upper_cou=0
for i in word:
    if i.islower():
        lower_cou +=1
    else:
        upper_cou +=1

if lower_cou >= upper_cou:
    print(word.lower())
else:
    print(word.upper())