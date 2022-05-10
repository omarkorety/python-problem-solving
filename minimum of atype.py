def find_smallest(lst,target_type):
    lst2 = []

    lst2 = [ i for i in lst  if type(i) == target_type]
    return min(lst2)





if __name__ == '__main__':
    lst=[10,-2.5,20,5,'mostafa',5.2,'Zu
    iad']
    print(find_smallest(lst,type(0)))
    print(find_smallest(lst,type(0.0)))
    print(find_smallest(lst,type('')))

  
