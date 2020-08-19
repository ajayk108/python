'''range'''
m =list(range(1,10))
print(m)
print('----------------------')

'''count technique'''
index_count =0
for letter in 'abcdefghijkl':
    print('at the index %s the letter is %s' % (index_count,letter))
    index_count += 1

print('-----------------------')

word = 'abcdefghijkl'
count = 0
for letter in word:
    print(word[count])
    count +=1

print('-----------------------')

''' enumerate'''
word = 'calendar'
for item in enumerate(word):
    print(item)

print('-----------------------')

''' zip '''
mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]
#print in list
print(list(zip(mylist1,mylist2,mylist3)))
print('\n')
#using for loop for zip lists
for item in zip(mylist1,mylist2,mylist3):
    print(item)

print('-----------------------')

'''unpacking zip'''''
for a,b,c in zip(mylist1,mylist2,mylist3):
    print(a)
    print(b)
    print(c)
    print('\n')

'''True of False'''
print(1 in [1, 2, 3])
print('a' in 'a word is there')

print('-----------------------')

'''dictionaries'''
d = {'k':123, 'k2':456}
print(123 in d.values())
print(456 in d.keys())
print('-----------------------')

''' min max'''
mylist5 = [10, 20, 30, 40, 50]
print(min(mylist5))
print(max(mylist5))

print('-----------------------')


''' import'''
from random import shuffle
mylist6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(mylist6)
print(mylist6)
 
from random import randint
print(randint(0,100))

print('-----------------------')

a =input('enter your name :')
print('your name is %s' % (a))
print(type(a))

num = int(input('enter your favorite no :'))
print('your favorite no is %s' % (num))
print(type(num))











