user_input = int(input())
nums = []
added_nums = 0

while user_input != 0:
    nums.append(user_input)
    user_input = int(input())
nums.sort()
print(*nums, sep="\n")
