mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 1, 2, 3, 4, 2, 2, 3, 3, 4]
mylist.append(12)
print(mylist)
print('-----------------------')

mylist.pop()
print(mylist)

print('-----------------------')
 
mylist.remove(1)
print(mylist)

print('-----------------------')

mylist.reverse()
print(mylist)

print('-----------------------')

mylist.sort()
print(mylist)

print('-----------------------')

m1 = mylist.copy()
print(m1)

print('-----------------------')

m1.clear()
print(m1)
print(mylist)

print('-----------------------')

count = mylist.count(3)
print(count)

print('-----------------------')

cars = ['ford', 'BMW', 'volvo']
cars.extend(mylist)
print(cars)

print('-----------------------')

mylist.insert(0, 50)
print(mylist)

print('-----------------------')

print(mylist)