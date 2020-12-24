f = open("data.txt", "r")
all_lines = f.readlines()


def clean(x):
    return x.replace("\n", "")


def get_acc(all_lines):
    visited_list = []
    leng = len(all_lines)
    i = 0
    total_acc = 0
    while i not in visited_list:
        if i < (leng):
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
        else:
            break
    return total_acc


def go_through_list_and_find_where_loop_starts(all_lines):
    visited_list = []
    leng = len(all_lines)
    i = 0
    total_acc = 0
    while i not in visited_list:
        if i < (leng-1):
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
        else:
            visited_list = "YES"
            break
    return visited_list

# then go to all the indexes in the above list one by one
# if it is nop change to jmp & vice versa. if acc then ignore in the all_lines list
# then go through the new all_lines list after changing and see if it goes ifinite
# if it goes infinite then go the next index in the suspects list
# do this until you find a version of all_lines which terminates
# once done output that version and use the method used in level 1 to get the answer


all_lines = list(map(clean, all_lines))
suspects = go_through_list_and_find_where_loop_starts(all_lines)

final_all_lines = []

temp_all_lines = all_lines.copy()
suspect_i = 0
while final_all_lines == []:
    j = suspects[suspect_i]
    to_change = all_lines[j]
    code = to_change[:3]
    n = to_change[4:]

    # ignore if code is acc, just go to the next suspect_i
    if code != "acc":
        if code == "nop":
            temp_all_lines[j] = f"jmp {n}"
        elif code == "jmp":
            temp_all_lines[j] = f"nop {n}"

        chck = go_through_list_and_find_where_loop_starts(temp_all_lines)

        # this means this is the correct change in code
        if chck == "YES":
            final_all_lines = temp_all_lines.copy()
        else:
            # it was an infinite loop again, so go to the next suspect
            suspect_i += 1
            # change the temp_all_lines to the normal one again
            temp_all_lines = all_lines.copy()
    else:
        suspect_i += 1


total_acc = get_acc(final_all_lines)
print("Level 2 Answer: ", str(total_acc))
