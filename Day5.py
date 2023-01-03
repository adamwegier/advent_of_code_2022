my_file = open(r"C:\Users\AWEGIER\Documents\Projects\adventOfCode\Input Files\Day 5\input.txt", "r")
data = my_file.read()
data_into_list = data.split('\n')

tree_index = data_into_list.index("")
tree_data = data_into_list[:tree_index]
move_data = data_into_list[-tree_index:]

s0 = s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = []

from itertools import groupby
p = []
for i in tree_data:
    p.append([(k, sum(1 for i in g)) for k,g in groupby(i.split(" "))])
rp = p[::-1][1:]

index_count = 0

tree