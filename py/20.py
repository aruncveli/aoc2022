from typing import Iterator

from more_itertools import ncycles


def calculate(part: int) -> int:
    assert part == 1 or part == 2

    numbers = []
    numbers_len = 0
    with open('../input/20') as file:
        for line in file:
            number = int(line)
            if part == 2:
                number *= 811589153
            numbers.append(number)
            numbers_len += 1

    indices: list[int] = list(range(numbers_len))
    cycle: list[int] | Iterator[int] = []
    if part == 1:
        cycle = iter(indices.copy())
    elif part == 2:
        cycle = ncycles(indices.copy(), 10)

    for i in cycle:
        number = numbers[i]
        if number == 0:
            continue
        current_index = indices.index(i)
        new_index = (current_index + number) % (numbers_len - 1)
        indices.pop(current_index)
        indices.insert(new_index, i)

    numbers = list(map(numbers.__getitem__, indices))
    zero_index = numbers.index(0)
    coordinate_sum = 0
    for offset in (1000, 2000, 3000):
        coordinate_sum += numbers[(zero_index + offset) % numbers_len]
    return coordinate_sum


print('Part 1:', calculate(1))
print('Part 2:', calculate(2))
