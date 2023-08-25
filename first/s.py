def f(lst):
    return lst.count(lst[0]) == len(lst)
 
print(f([12, 12, 12, 12]))