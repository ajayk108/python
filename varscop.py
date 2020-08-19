x = 50
def scop(x):
    print(f'the x is {x}')
    #local variable
    x = 200
    print(f'the x inseide function is {x}')

print(x)
scop(x)
print(x)
print('----------------------------------')

def scop2():
    global x
    print(f'the x is {x}')
    #local variable
    x = 200
    print(f'the x inseide function is {x}')

print(x)
scop2()
print(x)