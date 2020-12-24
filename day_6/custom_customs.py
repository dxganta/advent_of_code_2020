f = open("data.txt", "r")

all_lines = f.readlines()

data = []
curr_data = ""
for i in range(len(all_lines)):
    if all_lines[i] == "\n":
        data.append(curr_data)
        curr_data = ""
    else:
        curr_data += all_lines[i].replace("\n", "").replace(" ", "")

final_ans = 0
for d in data:
    unique_chars = "".join(set(d))
    final_ans += len(unique_chars)

print("Final Answer Level 1 : " + str(final_ans))
