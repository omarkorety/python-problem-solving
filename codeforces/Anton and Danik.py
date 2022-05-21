n=int(input())
k=list(input())
cou_ant=k.count("A")
cou_dan=k.count("D")
if cou_ant >cou_dan:
    print("Anton")
elif cou_dan > cou_ant:
    print("Danik")
else:
    print("Friendship")


