from itertools import combinations

f = open("data.txt", "r")

all_lines = f.readlines()


def check_if_any_2_equals_to_val(arr, val):
    final_ans = False
    for x, y in combinations(arr, 2):
        if x+y == val:
            final_ans = True
            break
    return final_ans


def clean(x):
    return int(x.replace("\n", ""))


nums = list(map(clean, all_lines))

preamble = 25
weakness = 0
weakness_ind = 0
for n in range(preamble, len(nums)):
    # check if sum of any two of the previous 5 numbers equals to n
    if check_if_any_2_equals_to_val(nums[(n-preamble):n], nums[n]) == False:
        weakness = nums[n]
        weakness_ind = n
        break

print(weakness_ind)
print("Final Answer Level 1 : ", weakness)
