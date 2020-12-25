from itertools import combinations

f = open("data.txt", "r")

all_lines = f.readlines()


def give_all_contigous_sets(arr, nums_req):
    contigus_arrs = []
    for i in range(len(arr)-(nums_req-1)):
        contigus_arrs.append(arr[i: i+(nums_req)])
    return contigus_arrs


def check_if_any_contigous_n_equals_to_val(arr, val, num_of_elems):
    final_ans = False
    for ls in give_all_contigous_sets(arr, num_of_elems):
        if sum(ls) == val:
            final_ans = ls
            break
    return final_ans


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

# level 2
weak_arr = nums[:weakness_ind]
ans_arr = []
for i in range(2, weakness_ind):
    temp_ans = check_if_any_contigous_n_equals_to_val(weak_arr, weakness, i)
    if temp_ans != False:
        ans_arr = temp_ans
        break

print(f"Final Answer Level 2 :  {max(ans_arr)+min(ans_arr)}")
