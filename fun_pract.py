def lesser_of_two_evens(a, b):
    if a%2==0 and b%2 ==0:
        # Both numbers are even
        if a < b:
            result = a
        else:
            result = b
    else:
        # one or both numbers are ODD
        if a > b:
            result = a
        else:
            result = b
    return result

r1 = lesser_of_two_evens(2, 4)
r2 = lesser_of_two_evens(7, 5)
print(r1)
print(r2)

print('-----------------------------------------')

'''using min max'''
def lesser_of_two_even(a,b):
    if a%2 == 0 and b%2 == 0:
        result = min(a,b)
    else:
        result = max(a,b)
    return result

r1 = lesser_of_two_even(2, 6)
r2 = lesser_of_two_even(7, 99)
print(r1) 
print(r2)

print('-----------------------------------------')

def animal_crackers(name):
    nm = name.lower().split()
    print(nm)
    first = nm[0]
    second = nm[1]
    return first[0] == second[0]

result = animal_crackers('Cat cow')
print(result)

print('-----------------------------------------')


def animal_crackers1(name):
    nm = name.lower().split()
    print(nm)
    return nm[0][0] == nm[1][0]

result0 = animal_crackers1('Cat cow')
print(result0)

print('-----------------------------------------')

''' makes twenty '''
def makes_twenty(n1, n2):
    if (n1+n2) == 20:
        return True
    elif n1 == 20:
        return True
    elif n2 == 20:
        return True
    else:
        return False

result1 = makes_twenty(12,8)
result2 = makes_twenty(20,8)
result3 = makes_twenty(10,8)
print(result1)
print(result2)
print(result3)

print('-----------------------------------------')

''' makes twenty '''
def makes_twenty1(n1, n2):
    return (n1+n2)==0 or n1==0 or n2==0
        
result11 = makes_twenty(12,8)
result22 = makes_twenty(20,8)
result33 = makes_twenty(10,8)
print(result11)
print(result22)
print(result33)

''' capitalize.....////////////////////////////'''
 
def cap(name):
     first =name[0]
     inbetween = name[1:3]
     fourth = name[3]
     rest = name[4:]
     return first.upper() + inbetween + fourth.upper() + rest

res = cap('macdonald')
print(res)

def cap2(name):
    first = name[:3]
    fourth = name[3:]
    return first.capitalize() + fourth.capitalize()


res1 = cap2('macdonald')
print(res1)

print('-----------------------------------------')

'''revese word or sentense ///using joint method///////////'''

def joint(mystring):
    print(mystring)
    word_split = mystring.split()
    reverse_string = word_split[::-1]
    return ' '.join(reverse_string)

res4 = joint('i am lazy')
print(res4)

print('-----------------------------------------')

'''absolute value....'''
def almost_there(n):
    return (abs(100-n) <= 10) or  (abs(200-n)<= 10)

res6 = almost_there(104)
res7 = almost_there(150)
res8 = almost_there(209)
print(res6)
print(res7)
print(res8)

print('-----------------------------------------')


'''finding 33 '''
def has_33(num):
    for i in range(0,len(num)-1):
        if num[i] == 3 and num[i+1] == 3:
            return True

    return False

resl = has_33([1, 3, 7, 4])
resl2 = has_33([1, 3, 3, 4])
print(resl)
print(resl2)

print('-----------------------------------------')

'''string trice ex. hhheeellllllooo......'''
def paper_doll(mystring):
    result = ''
    for st in mystring:
        result += st*3
    return result

ress = paper_doll('ajay')
print(ress)

print('-----------------------------------------')

''' Blackjack '''
def blackjack(a, b, c):
    if sum([a,b,c]) <=21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <=31:
        return sum([a,b,c])-10
    else:
        return 'BUST' 

ress1 =blackjack(5, 6, 7)
ress2 =blackjack(9, 9, 9)
ress3 =blackjack(9, 9, 11)
print(ress1)
print(ress2)
print(ress3)

print('-----------------------------------------')

'''69'''

def summer_of_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
                break
        while not add:
            if num != 9:    
                break
            else:
                add = True
                break
    return total

r = summer_of_69([2, 1, 6, 9, 11])
print(r)

print('-----------------------------------------')

'''spy game 007//////////////////'''

def spy_game(nums):
    code=[0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1

re1 = spy_game([1, 2, 0, 4, 0, 7])
print(re1)