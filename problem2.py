try:
    n = int(input())
    numbers = []
    if n >= 5:
        for _ in range(n):
            try:
                user_input = int(input())
                if user_input < 0:
                    print("A negative number found")
                    break
                numbers.append(user_input)
            except ValueError:
                print("Not a number")
                break
        print(numbers)
        numbers_copy = numbers.copy()
        numbers_copy.remove(min(numbers_copy))
        numbers_copy.remove(min(numbers_copy))
        numbers_copy.remove(max(numbers_copy))
        numbers_copy.remove(max(numbers_copy))
        print(numbers_copy)
    else:
        print("You need at least 5 numbers")
except ValueError:
    print("N is not a number")
