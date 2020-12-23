f = open("data.txt", "r")

all_lines = f.readlines()


def get_row(b_pass):
    total_rows = 128
    start = 0
    end = total_rows - 1
    i = 0
    while end-start > 0:
        mid = ((end-start) // 2) + start  # start to mid, mid+1 to end
        if b_pass[i] == "F":
            end = mid
        elif b_pass[i] == "B":
            start = mid+1
        i += 1

    return start


def get_col(b_pass):
    b_pass = b_pass[-3:]
    total_cols = 8
    start = 0
    end = total_cols - 1
    i = 0
    while end-start > 0:
        mid = ((end-start) // 2) + start  # start to mid, mid+1 to end
        if b_pass[i] == "L":
            end = mid
        elif b_pass[i] == "R":
            start = mid+1
        i += 1

    return start


seat_ids = []

for i in range(len(all_lines)):
    b_pass = all_lines[i].replace("\n", "")
    seat_id = get_row(b_pass)*8 + get_col(b_pass)
    seat_ids.append(seat_id)


print("FINAL ANSWER LEVEL 1 : " + str(max(seat_ids)))
x = sorted(seat_ids)
level_2_ans = 0
for i in range(len(seat_ids)-1):
    if x[i+1] - x[i] != 1:
        print("FINAL ANSWER LEVEL 2:" + str(x[i]+1))
