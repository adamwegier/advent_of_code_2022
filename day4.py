my_file = open(r"C:\Users\AWEGIER\Documents\Projects\adventOfCode\Input Files\Day 4\input.txt", "r")
data = my_file.read()
data_into_list = data.split('\n')

import re


def partOne():
    v = 0
    for line in open(r"C:\Users\AWEGIER\Documents\Projects\adventOfCode\Input Files\Day 4\input.txt"):
        a, b, c, d = map(int, re.findall('\d+', line))

        if a <= c and b >= d or c <= a and d >= b:
            v += 1

    return(v)


def partTwo():
    v = 0
    for line in open(r"C:\Users\AWEGIER\Documents\Projects\adventOfCode\Input Files\Day 4\input.txt"):
        a, b, c, d = map(int, re.findall('\d+', line))

        if c <= a <= d or c <= b <= d or a <= c <= b or a <= d <= b:
            v += 1

    return(v)

print(partTwo())