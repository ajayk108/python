'''num is in range or not '''
def ran_check(num, low, high):
    if num in range(low, high):
        print('%s is in the range' % (num))
    else:
        print('the number is the outside the range')

ran_check(5,1,10)

''' no of uppercases and lowercases '''
def uplow(mystring):
    up =0
    low =0
    for st in mystring:
        if st.isupper():
            up += 1
        elif st.islower():
            low +=1
        else:
            pass
    print('original stirng : %s' % (mystring))
    print('num of upper case letters are : %d' % (up))  
    print('num of lower case letters are : %d' % (low))

s ="This is The String which I soterd in Variable s"
uplow(s)

print('--------------------------------------------------')

'''unique element of the first list '''
def uique_list(num):
    x = []
    for n in num:
        if n not in x:
            x.append(n)
    return x

l = [1,1,1,2,2,3,3,4,4,5,5,6,6,6,6,7,7,]
result = uique_list(l)
print(result)

print('--------------------------------------------------')

''' multiplication of list elements'''
def multiplication(mylist):
    total = mylist[0]
    for num in mylist:
        total *= num
    return total

ls = [1, 2, 4, 6,]
res = multiplication(ls)
print(res)

'''whether passed string is palindrom or not '''
def palindrome(mystring):
    if mystring == mystring[::-1]:
        print("string is Palindrome")
    else:
        print('string is Not Palindrome')

palindrome('madam')
palindrome('ajay')





