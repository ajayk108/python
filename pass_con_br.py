''' pass'''
mylist =[1, 2, 3, 4, 5]
for num in mylist:
    #comment
    pass

print('the end of script')

print('----------------------------------')

'''continue'''
for string in 'hello':
    if string =='e':
        continue
    print(string)

print('----------------------------------')

'''break'''
for string in 'hello world':
    if string == ' ':
        break
    print(string)

print('----------------------------------')

''' break using while'''
x = 0
while x < 5:
    if x == 3:
        break
    print(x)
    x += 1
