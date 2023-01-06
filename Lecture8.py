num_list = [1, 2, 3]  # create a list
print(num_list)  # indexes in lists start from 0 and reverse from -1
print(type(num_list))  # prints type
print(id(num_list))  # shows id in heap
print(num_list[1])  # prints element 2
list = [2, 3.2, "hello", True]
list_in_list = [5, "hello", [2, "world"], True]  # list in list
print(list_in_list[2][1])  # taking info from the list in the list
list_in_list[2] = "new"  # changing the index with new value
print(list_in_list)
a = [5, 10]
a_copy = a[:]  # this is deep copy with self ID in the memory(we can make copy this way saving the first values)
b = a  # note that copies of variable list points to same id in the heap!!!!
print(id(a))  # same ID as b
print(id(b))  # same ID as a
b[1] = 11  # if you change value in copy it will change the original value as well
print(a)  # same value as b
print(b)  # same value as a
print(a_copy)
print(len(list_in_list))  # len can show how many items you have in list

# slicing has same purpose ( start is 0 and step is 1)

# .append-function to insert value in end of list
list_in_list.append("new item")  # append always adds in the end of list
print(list_in_list)

# .insert-function to insert a value in list on particular index
words = ["ball", "base"]
words.insert(0, "gloves")  # the function needs index where to put the new value
print(words)

# .pop-function to remove a value from list
words.pop(0)  # removes value from first index (0)
print(words)  # prints with removed "gloves"
removed_words = words.pop(0)  # saves the value of removed item
print(words)  # prints with removed "ball"
print(removed_words)  # prints the removed item from original list

# .remove-function to remove a value by its name
# if the name is not found in the list it will give error
# to avoid error use 'try' 'except' function
sports = ["soccer", "baseball", "swimming", "hockey"]
try:
    sports.remove("soccer")
except:
    print("That item does not exist in list")
print(sports)
l = [1, 2, 3, 4, 5, 5, 5, 5]
print(l)
for each in range(l.count(5)):  # removes all 5 with cycle
    l.remove(5)
print(l)
print({*l})  # set remove duplicates
# extra functions for lists are min,max,sum for numbers in lists
nums = [1, 4, 3, 2, 5]
print(min(nums))  # prints min number of list
print(max(nums))  # prints max number of list
print(sum(nums))  # prints sum of the list

# nums = sorted(nums)   sorts from low to high num
nums.sort()
print(nums)
print(sorted(nums, reverse=True))  # this will reverse sort value

if 10 in nums:  # another search operation
    print("There is 10")
else:
    print("10 not found")

# list comprehension
# user_input = []
# for i in range(5):
#    num = int(input())
#    user_input.append(num)

# print(user_input)

user_input = [i ** 2 for i in range(5)]  # list comprehension with cycle
print(user_input)

user_input = [i ** 2 for i in range(2, 10) if (i ** 2) % 2 == 0]  # list comprehension with cycle and condition
print(user_input)
