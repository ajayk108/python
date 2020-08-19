a = 8
b = 2
try:
    print(a/b)
except Exception:
    print('you cannot divide the number by zero')

print('---------------------------------------------')

try:
    print('resource opened...')
    print(a/b)
except Exception as e:
    print('you can not divide the number by zero',e)
finally:
    print('resource closed...')

print('---------------------------------------------')

try:
    print('resource opened...')
    print(a/b)
    k = int(input('enter the interger : '))
    print(k)
except ZeroDivisionError:
    print('you can not divide the number by zero')
except ValueError:
    print('input type error')
except Exception:
    print('Something went wrong...')
finally:
    print('resource closed...')
