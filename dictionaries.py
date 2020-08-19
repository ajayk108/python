k = {'key1':'value1', 'key2':'value2'}
print(k)
print(k.keys())
print(k.values())
print(k.items())

k= {'k1':'val1', 'k2':{'insidekey':'INSIDEVAL'}}

print(k['k1'])
print(k['k2']['insidekey'])
print(k['k1'].upper())
print(k['k2']['insidekey'].lower())
k['k3']='newvalue'
print(k)
