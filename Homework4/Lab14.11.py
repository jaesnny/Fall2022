# JenniferChu
# 1873159

def selection_sort_descend_trace(num_list):
    for i in range(len(num_list) - 1):
        max_num = i
        for j in range(i + 1, len(num_list)):
            if num_list[max_num] < num_list[j]:
                max_num = j
        num_list[i], num_list[max_num] = num_list[max_num], num_list[i]

        reform_list = ' '.join(str(v) for v in num_list)
        print(reform_list, end=' \n')


if __name__ == "__main__":
    num = []
    number = [int(x) for x in input().split()]

    selection_sort_descend_trace(number)
