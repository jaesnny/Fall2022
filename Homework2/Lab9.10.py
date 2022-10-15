#JenniferChu
#1873159
import csv
from typing import TextIO

input_filename: str = input()
file_mine: TextIO
with open(input_filename, 'r') as file_mine:
    word = csv.reader(file_mine, delimiter=',')
    diction = dict()
    for i in word:
        for j in i:
            if j in diction:
                diction[j] = diction[j] + 1
            else:
                diction[j] = 1
    for n in list(diction.keys()):
        print("{} {}".format(n, diction[n]))
