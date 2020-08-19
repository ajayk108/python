mylist = [1, 3, 2, 4, 5, 9, 6, 10, 7, 8]
for num in sorted(mylist):
    print(num)

print('------------------------------------------')

mylist.sort()
for num in mylist:
    if num % 2 == 0 :
        print(num) 
    else:
        print(f'odd num: {num}')
    
print('------------------------------------------')

sum1 = 0
for num in mylist:
    sum1 += num

print(sum1)

print('------------------------------------------')

#stirngs
for item in 'hello world':
    print(item)

print('------------------------------------------')

tup = (1, 'python', '2', 'cpp')
for items in tup:
    print(items)

print('------------------------------------------')

#tuples inside lists
mylist2 = [(1,2), (3,4), (5,6), (7,8), (9,10)]
print('length of mylist2 is {}'.format(len(mylist2)))
print('length of mylist2 is %d' % (len(mylist2)))
for items in mylist2:
    print(items)

print('------------------------------------------')

'''tuples and packing'''
mylist3 = [(1,2), (3,4), (5,6), (7,8), (9,10)]
for a,b in mylist3:
    print(a)
    print(b)

print('------------------------------------------')

''' Dictionaries and packing'''
d ={'k1':'c', 'k2':'cpp', 'k3':'php', 'k4':'python'}
for key,value in d.items():
    print(key)
    print(value)

print('------------------------------------------')
