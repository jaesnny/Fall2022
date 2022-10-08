#JenniferChu
#1873159

mypassword = input()
password = ''
for i in mypassword:
    if i == 'i':
        password += '!'
    elif i == 'a':
        password += '@'
    elif i == 'm':
        password += 'M'
    elif i == 'B':
        password += '8'
    elif i == 'o':
        password += '.'
    else:
        password += i
password += 'q*s'
print(password)
