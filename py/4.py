import re

part_1_result = 0
part_2_result = 0

with open('../input/4') as file:
    for line in file:
        l1, r1, l2, r2 = map(int, re.split(r'[,-]', line))
        if (l1 <= l2 and r1 >= r2) or (l2 <= l1 and r2 >= r1):
            part_1_result += 1
        if (l2 <= r1) and (l1 <= r2):
            part_2_result += 1

print('Part 1:', part_1_result)
print('Part 2:', part_2_result)
