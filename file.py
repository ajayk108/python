myfile = open('1.txt','r')
contents = myfile.read()
print(contents)
myfile.close()

with open('2.txt', 'w') as myfile:
    str1=input('write the contents :')
    myfile.write(str1)

with open('1.txt', 'a') as myfile:
    str1= input('append the contents :')
    myfile.write(str1)

with open('1.txt', 'r') as myfile:
    print(myfile.read()) 