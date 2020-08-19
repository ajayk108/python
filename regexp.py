import re

nameage = '''
Ajay is 21 Vijay is 21 Navin is 23 '''

ages = re.findall(r'\d[1-3]',nameage)
names = re.findall(r'[A-Z][a-z]*',nameage)
# dt = {}
for key, val in zip(names, ages):
    print(key,val)

print('===================================================')

if re.search('spiritual','i like spiritual books.'):
    print('There is a spiritual')

print('===================================================')

data = re.findall('inform', 'we need to inform him that information')

for d in data:
    print(d)

print('===================================================')

str = 'we need to inform him that information'

for i in re.finditer('inform', str):
    tup = i.span()
    print(tup)


print('===================================================')

str2 = 'sat, mat, hat, Pat'
 
allstr = re.findall('[smhp]at', str2)
for i in  allstr:
    print(i)