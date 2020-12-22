import re

f = open("data.txt", "r")
f2 = open("cleaned_data.txt", "w")
all_lines = f.readlines()
# 284

expected = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def list_to_dic(ls):
    dic = {}
    for e in ls:
        y = re.split(":", e)
        dic[y[0]] = y[1]
    return dic


def valid_or_not(given, expected):
    for f in expected:
        if f not in given:
            return False
    return True


final_data = []
curr_ls = []
curr_dic = {}
for i in range(len(all_lines)):
    if all_lines[i] == "\n":
        # final_data.append(curr_ls)
        # curr_ls = []
        final_data.append(curr_dic)
        curr_dic = {}
    else:
        x = re.split("\s", all_lines[i].replace("\n", ""))
        curr_dic.update(list_to_dic(x))


def level_1(final_data):
    final_answer = 0
    for d in final_data:
        if valid_or_not(d.keys(), expected):
            final_answer += 1
    print("Final Answer Level 1: " + str(final_answer))


def check_height(height, unit):
    if unit == "cm":
        if height >= 150 and height <= 193:
            return True
    elif unit == "in":
        if height >= 59 and height <= 76:
            return True
    return False


def check_haircolor(hcl):
    x = re.findall(r"#[a-f0-9]+", hcl)
    if len(x) == 1:
        if len(x[0]) == 7:
            return True
    return False


def check_eyecolor(ecl):
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if ecl in colors:
        return True
    return False


def check_pid(pid):
    if len(pid) == 9:
        return True
    return False


def level_2(final_data):
    final_answer = 0
    accepted = []
    for d in final_data:
        if valid_or_not(d.keys(), expected):
            if int(d["byr"]) >= 1920 and int(d["byr"]) <= 2002:
                if int(d["iyr"]) >= 2010 and int(d["iyr"]) <= 2020:
                    if int(d["eyr"]) >= 2020 and int(d["eyr"]) <= 2030:
                        # splitting hgt into number and word
                        x = re.findall(r"(\d+)(\w+)", d["hgt"])
                        height = int(x[0][0])
                        unit = x[0][1]
                        if check_height(height, unit):
                            if check_haircolor(d["hcl"]):
                                if check_eyecolor(d["ecl"]):
                                    if check_pid(d["pid"]):
                                        final_answer += 1
                                        accepted.append(d)
    print("Final Answer Level 2: " + str(final_answer))


level_1(final_data)
level_2(final_data)
