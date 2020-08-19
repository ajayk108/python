mylist = [num for num in range(0,11)]
print (mylist)

mylist = [num**2 for num in range(0,11) ]
print(mylist)

mylist = [num for num in range(0, 11) if num %2 == 0 ]
print (mylist)

'''celcius fahrenheit'''
celcius = [0, 10, 20, 30, 40.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit) 

print('-------------------')
mylist = []
for x in [1, 2, 3]:
    for y in [1, 100, 1000]:
        mylist.append(x * y)

print(mylist)

mylist = [x*y for x in [1, 2, 3] for y in [1, 100, 1000]]
print(mylist)