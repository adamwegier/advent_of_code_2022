my_file = open(r"C:\Users\AWEGIER\Documents\Projects\adventOfCode\Input Files\Day 3\input.txt", "r")
data = my_file.read()
data_into_list = data.split('\n')


def partOne(data):
    #find combined values in one list
    #enumerate alphabet twice
    #make dict and add?

    valueList = []
    for i in data:
        s1 = i[-int(len(i)/2):]
        s2 = i[:int(len(i)/2)]
        a = list(set(s1)&set(s2))
        for y in a:
            valueList.append(y)

    import string
    values = dict()
    for index, letter in enumerate(string.ascii_letters):
        values[letter] = index + 1

    print(f"My score is {sum([values[item] for item in valueList])}.")

partOne(data_into_list)

def partTwo(data):
    commonList = []
    for i in zip(*(iter(data),) * 3):
        a = (list(set(i[0]) & set(i[1]) & set(i[2])))
        for y in a:
            commonList.append(y)

    import string
    values = dict()
    for index, letter in enumerate(string.ascii_letters):
        values[letter] = index + 1

    print(f"My score is {sum([values[item] for item in commonList])}.")


partTwo(data_into_list)