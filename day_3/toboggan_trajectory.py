# f = open("data.txt", "r")
# f2 = open("appended_data.txt", "w")

# all_lines = f.readlines()

# for i in range(len(all_lines)):
#     print(i)
#     line = all_lines[i].replace('\n', '')
#     for i in range(325):
#         f2.write(line)
#     f2.write('\n')
#     print(line)

def get_trees(right, down, data):
    no_of_trees = 0
    curr_pos = 0
    for i in range(down, len(data), down):
        curr_pos += right
        if data[i][curr_pos] == "#":
            no_of_trees += 1
    return no_of_trees


def level_1(data):
    print("Final Answer Level 1: " + str(get_trees(3, 1, data)))


def level_2(data):
    ans = get_trees(1, 1, data) * get_trees(3, 1, data) * get_trees(5,
                                                                    1, data) * get_trees(7, 1, data) * get_trees(1, 2, data)
    print("Final Answer Level 2: " + str(ans))


f = open("appended_data.txt", "r")

data = f.readlines()

level_1(data)
level_2(data)
