numbers = [3, -4, 1, 0, -1, 0, -2]
# negatives = []
# zeros = []
# positives = []
# for num in numbers:
#    if num < 0:
#        negatives.append(num)
#    elif num == 0:
#        zeros.append(num)
#    else:
#        positives.append(num)
# print(*negatives, *zeros, *positives, sep="\n")
negatives = [num for num in numbers if num < 0]  # first index is what will be the end value
zeros = [num for num in numbers if num == 0]
positives = [num for num in numbers if num > 0]
print(*negatives, *zeros, *positives, sep="\n")
