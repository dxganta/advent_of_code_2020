import re

f = open("data.txt", "r")
all_lines = f.readlines()


def bags_to_map(inside_bags):
    temp_map = {}
    for b in inside_bags:
        n = b[0]
        color = b[2:]
        temp_map[color] = int(n)
    return temp_map

# first clean the data and make a dictionary out of it in the form
# { "shiny gold" : {"dark olive" :1, "vibrant plum" : 2} }


# cleaning data
main_map = {}
for line in all_lines:
    main_bag = re.findall(r"\w+ \w+", line)[0]
    inside_bags = re.findall(r"(\d \w+ \w+) bag", line)

    main_map[main_bag] = bags_to_map(inside_bags)

# print(main_map)


def recur_sol(bag_color):
    if main_map[bag_color] == {}:
        return 0
    else:
        total_bags = 0
        for k in main_map[bag_color].keys():
            temp_bags = main_map[bag_color][k]
            total_bags += temp_bags + (temp_bags * recur_sol(k))

    return total_bags


print("Final Answer Level 2 : ", recur_sol("shiny gold"))
