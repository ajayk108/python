''' positional argument'''
def say_hello(name):
    print('hello '+name)

say_hello('ajay')

''' default argument'''
def say_hello(name='vijay'):
    print('hello '+name)

say_hello()

'''fun with return type'''
def hello(name):
    return 'hello '+name

result =hello('chaya')
print(result)

''' addition '''
def add(n1, n2):
    return n1 + n2

result = add(20,30)
print(result)

'''word check in string'''
def spiritual_check(mystring):
    if 'spiritual' in mystring:
        return True
    else:
        return False

result = spiritual_check('i like spiritual')
print(result)

''' word check with simple technique'''
def spiritual_check1(mystring):
    return 'spiritual' in mystring

result = spiritual_check1('i like spiritual')
print(result)

'''pig latin'''
def pig_latin(word):
    first_letter =word[0]
    if first_letter in 'aeiou':
        pig_word = word +'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word

result = pig_latin('apple')
print(result)

''' *args ///////////////////////////////////// '''

def myfunc(*args):
    #Returns 5% of the sum 
    return sum(args) * 0.05

result = myfunc(40, 60)
print(result)

def myfun2(*args):
    for num in args:
        print(num)

myfun2(10, 20, 30, 40, 50)

''' **kwargs////////////////////////////////////////////////'''
def myfunc3(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('my favorite fruit is %s' %(kwargs['fruit']))
    else:
        print('i did not find any fruit here..')

myfunc3(fruit='apple', drink='water')

def myfunc4(**kwargs):
    print(kwargs)
    for key,val in kwargs.items():
        print(key)
        print(val)
        print('\n')
   
myfunc4(a='cpp', b='python', c='phps')

''' *args **kwargs //////////////////////'''
def myfunc5(*args, **kwargs):
    print(args)
    print(kwargs)
    print('i would like to read %d %s books' % (args[1],kwargs['book']))
    for key,val in kwargs.items():
        print(key,end=" ")
        print(val)
    for num in args:
        print(num)

myfunc5(1, 2, 3, animal='dog', book='spiritual', food='satvik')




