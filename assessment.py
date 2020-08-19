# number
print((62 +(10 ** 2) / 4 * 7)-136.75)

#type of the result of the expression
print(type(3+1.5+4))

# square , square root
print(25 ** 0.5)
print(64 ** 0.5)
print(81 **0.5 )
#square
print(4 **2)
print(8 ** 2) 
print(5 ** 2)

# print out 'e' using index
s = 'hello'
print(s[1])

#Reverse the string using hello
print(s[::-1])

#print out the 'o' using two methods
print(s[4])
print(s[-1])

#buit the list[0,0,0] two ways
print([0]*3)
lst = [0, 0, 0]
print(lst)

#reaasign 'hello' in this nested list to say 'goodbye' insted

list2 = [1, 2, [3, 4,'hello']]
print(list2)
list2[2][2]= 'goodbye'
print(list2)

#sort the list
list3 = [1, 4, 5, 6, 3, 2, 7]
list3.sort()
print(list3)
print(sorted(list3))
 
 #grab the hello from dictionaries
d = {'key':'hello'}
print(d['key'])
d = {'key':{'key2':'hello'}}
print(d['key']['key2'])
d = {'key':[{'nestkey':['this is deep', ['hello']]}]}
print(d['key'][0]['nestkey'][1][0])

d = {'key':[1, 2, {'key2':['this is tricky', {'tough':[1, 2, ['hello']]}]}]}
print(d['key'][2]['key2'][1]['tough'][2][0])

#tuples
t = (1, 'hello', 2, 'welcome')
print(t)

# sets
list4 = [1, 2 , 44, 22, 12 ,33, 33, 55, 33, 4, 3, 1, 2 ]
s = set(list4)
print(s)

# Boolean output
l_one = [1, 2, [6, 4]]
l_two = [1, 2, {'k1': 4}]

#True of False
print(l_one[2][0] >= l_two[2]['k1'])