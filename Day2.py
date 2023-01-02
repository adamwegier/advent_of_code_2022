#Not happy with this brute force!

my_file = open(r"C:\Users\AWEGIER\Documents\Projects\adventOfCode\Input Files\Day 2\input.txt", "r")
data = my_file.read()
data_into_list = data.split('\n')

#Opponent
# A = Rock
# B = Paper
# C = Scissors

#Me
# X = Rock (+1)
# Y = Paper (+2)
# Z = Scissors (+3)

#Points
# Loss = 0
# Draw = 3
# Win = 6

def partOne(data):
    count = 0
    for i in data_into_list:
        if i == 'A X':
            count += 4
        elif i == 'A Y':
            count += 8
        elif i == 'A Z':
            count += 3
        elif i == 'B X':
            count += 1
        elif i == 'B Y':
            count += 5
        elif i == 'B Z':
            count += 9
        elif i == 'C X':
            count += 7
        elif i == 'C Y':
            count += 2
        elif i == 'C Z':
            count += 6

    return(count)

# X = Lose
# Y = Draw
# Z = Win



def partTwo(data):
    count = 0
    for i in data_into_list:
        if i == 'A X':
            count += 3
        elif i == 'A Y':
            count += 4
        elif i == 'A Z':
            count += 8
        elif i == 'B X':
            count += 1
        elif i == 'B Y':
            count += 5
        elif i == 'B Z':
            count += 9
        elif i == 'C X':
            count += 2
        elif i == 'C Y':
            count += 6
        elif i == 'C Z':
            count += 7
    return (count)

print(partTwo(data_into_list))