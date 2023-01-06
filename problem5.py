import random

ticket = []
# for i in range(6):
#    num = random.randint(1, 49)
#    while num in ticket:
#        num = random.randint(1, 49)
#    ticket.append(num)
# print(*ticket)
i = 0
while i < 6:
    next_number = random.randint(1, 49)
    if next_number not in ticket:
        ticket.append(next_number)
        i += 1
print(*ticket)
