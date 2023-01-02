#PART 1

my_file = open(r"C:\Users\AWEGIER\Documents\Projects\adventOfCode\Input Files\Day 1\input.txt", "r")
data = my_file.read()
data_into_list = data.split('\n')

#return most calories in a list of elves carrying foods with calories
def partOne(data):
    z = 0
    count = 0
    for i in range(0, len(data)-1):
        if data[i] == '':
            if count > z:
                z = count
            count = 0
        else:
            count += int(data[i])

    return(z)

#return sum of top 3 calories carried by elves
def partTwo(data):
    count = 0
    countList = []
    for i in range(0, len(data) - 1):
        if data[i] == '':
            countList.append(count)
            count = 0
        else:
            count += int(data[i])

    countList.sort()
    return(sum(countList[-3:]))



print(partOne(data_into_list))
print(partTwo(data_into_list))








my_file.close()

