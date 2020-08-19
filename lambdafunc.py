'''map function'''
def mapfun(mystring):
    if len(mystring)%2 == 0:
        return 'Even'
    else:
        return mystring[0]

names = ['ajay', 'vijay', 'navin']#///////////////////////////////////////////

result = list(map(mapfun, names))
print(result)

print('-------------------------------')

''' fileter function'''
def filters(num):
    return num%2 == 0

mynum = [1,2,3,4,5,6,7,8]#///////////////////////////////////////////////////////

result1 = list(filter(filters, mynum))
print(result1)

for n in filter(filters, mynum):
    print(n) 

print('-------------------------------')

''' lambda expression /////////////////'''

l = lambda num: num%2 == 0 
e = l(2)
print(e)

print('-------------------------------')

''' lambda using map'''
result2 = list(map(lambda num: num*2 ,mynum))
print(result2)
result4 = list(map(lambda num: num[0], names))
print(result4)

print('-------------------------------')

''' lambda using filter fun '''
result3 =list(filter(lambda num: num%2 == 0, mynum))
print(result3)

print('-------------------------------')


    









