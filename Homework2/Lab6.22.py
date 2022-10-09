# JenniferChu
# 1873159

cox = int(input())
coy = int(input())
answer = int(input())
cox2 = int(input())
coy2 = int(input())
answer2 = int(input())
x = 0
y = 0
check = False
# cox * x + coy * y = answer
# cox2 * x + coy2 * y = answer2
for x in range(-10, 10, 1):
    for y in range(-10, 10, 1):
       if (cox * x) + (coy * y) == answer and (cox2 * x) + (coy2 * y) == answer2:
           check = True
           print(x, y)
if check == False:
    print('No solution')
