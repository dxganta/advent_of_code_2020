import re


def level_1(data):
    answer = 0

    for i in range(len(data)):
        seq = data[i]
        x = re.findall(r"(\d+)-(\d+) (\w): (\w+)", seq)
        minm = x[0][0]
        maxm = x[0][1]
        letter = x[0][2]
        passwd = x[0][3]

        occs = passwd.count(letter)

        if (occs >= int(minm)) and (occs <= int(maxm)):
            answer += 1
    print("Final Answer Level 1: " + str(answer))


def level_2(data):
    answer = 0
    for i in range(len(data)):
        seq = data[i]
        x = re.findall(r"(\d+)-(\d+) (\w): (\w+)", seq)
        pos_1 = int(x[0][0]) - 1
        pos_2 = int(x[0][1]) - 1
        letter = x[0][2]
        passwd = x[0][3]

        if ((passwd[pos_1] == letter and passwd[pos_2] != letter) or (passwd[pos_2] == letter and passwd[pos_1] != letter)):
            answer += 1
    print("Final Answer Level 2: " + str(answer))


f = open("data.txt", "r")
data = f.readlines()

level_1(data)
level_2(data)
