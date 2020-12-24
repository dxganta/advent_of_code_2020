f = open("data.txt", "r")
all_lines = f.readlines()


def clean(x):
    return x.replace("\n", "")


all_lines = list(map(clean, all_lines))


def get_acc(all_lines):
    visited_list = []
    i = 0
    total_acc = 0
    while i not in visited_list:
        visited_list.append(i)
        inst = all_lines[i]
        code = inst[:3]
        n = inst[4:]
        if code == "nop":
            i += 1
        elif code == "acc":
            i += 1
            total_acc += int(n)
        elif inst[:3] == "jmp":
            i += int(n)
    return total_acc


total_acc = get_acc(all_lines)
print("Level 1 Answer: ", str(total_acc))

# program terminates if i becomes greater than the length of all_lines list
