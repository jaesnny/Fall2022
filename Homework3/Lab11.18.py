# JenniferChu
# 1873159

int_input = map(int, input().split())
int_list = []
for i in int_input:
    if i >= 0:
        int_list.append(i)
int_list.sort()
print(*int_list, sep=' ', end=' ')
