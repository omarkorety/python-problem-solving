name,age='mostafa',33
print("{} is {} years old".format(name,age))
print('{} is {age} years old'.format(name,age=age))
print('{0} is {age} years old'.format(name,age=age))
##   print('{1} is {age} years old'.format(name,age=age))

my_lst=['mostafa',33,1000]
print('{lst[0]} is {lst[1]} years old with salary{lst[2]}'.format(lst=my_lst))
print(','.join('A#B#C'.split('#')))



