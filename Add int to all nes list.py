def add_value(nest_lst,value):
    new_nest_lst=[]
    for lst in nest_lst:
        new_lst=[]
        for item in lst:
            new_lst.append(item+value)
        new_nest_lst.append(new_lst)
    return new_nest_lst



nest_lst=[[1,2],[2,3],[3,4],[4,5],[5,6],[8,1]]
new_lst=add_value(nest_lst,10)
print(new_lst)

################----OR------BY------list comprihantion-----

new_lst2=[[item+10 for item in lst]  for lst in  nest_lst] 
print(new_lst2)