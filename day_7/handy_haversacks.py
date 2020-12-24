import re

f = open("data.txt", "r")
all_lines = f.readlines()

to_finds = ["shiny gold"]

# first find all the bags that contain shiny gold bag directly
# remove them from the main list
# then for each bag that contains shiny gold bag directly find that bags that contain this bag
# remove them from the list
# continue this until you get no more bags

final_ans = 0
all_lines_copy = all_lines.copy()
while len(to_finds) > 0:
    got_bags = []
    for to_find in to_finds:
        for line in all_lines:
            if to_find in line:
                got_bags.append(re.findall(r"\w+ \w+", line)[0])
                all_lines_copy.remove(line)
        all_lines = all_lines_copy.copy()
    # remove shiny_gold if it is added
    for bag in to_finds:
        if bag in got_bags:
            got_bags.remove(bag)
    final_ans += len(got_bags)
    to_finds = got_bags.copy()


# print(got_bags)
# print(all_lines)
# print(to_finds)

print("Final Answer Level 1 : ", final_ans)
