'''split'''
st =  'print only the word that starts with s in sentense'
print(st.split())
for word in st.split():
    if word[0].lower()== 's':
        print(word)
        
print('----------------------------')
'''range'''
print(list(range(0,11,2)))
for num in range(0,11,2):
    print(num)
        
print('----------------------------')

'''comprehension'''
mylist = [x for x in range(1,51) if x%3 == 0]
print(mylist) 

print('----------------------------')

string = 'print every word in the sentense that has the even numbers of letters'
for st in string.split():
    if len(st)%2 == 0:
        print(st +' is even..!')

''' program  of fizz and fizbus'''
for num in range(1,101):
    if num%3 ==0 and num%5 ==0:
        print('FizzBuzz')
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)
print('----------------------------')

'''first letter of every word as string'''
st = 'Create a list of the first letters of every word in this string'

string = [s[0] for s in st.split() ]
print(string)



