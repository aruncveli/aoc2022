from collections import defaultdict
from copy import deepcopy
from functools import reduce

direction_char_to_complex = {'^': complex(0, -1), '>': complex(1, 0), 'v': complex(0, 1), '<': complex(-1, 0)}
direction_to_blizzards: dict[complex, set[complex]] = defaultdict(set)

with open('../input/24') as file:
    width = len(file.readline().strip())
    file.seek(0)

    for j, line in enumerate(file):
        for i, char in enumerate(line):
            if char in direction_char_to_complex:
                direction_to_blizzards[direction_char_to_complex[char]].add(complex(i - 1, j - 1))

height = j - 1
width = i - 1


def wrap_position(x: complex) -> complex:
    return complex(x.real % width, x.imag % height)


start = complex(0, -1)
end = complex(width - 1, height)
limits = (start, end)

goals = iter((end, start, end))
goal = next(goals)

possible_next_positions = {start}
minutes = 0
part = 1

while possible_next_positions:
    minutes += 1

    for direction, blizzards in deepcopy(direction_to_blizzards).items():
        direction_to_blizzards[direction].clear()
        for blizzard in blizzards:
            direction_to_blizzards[direction].add(wrap_position(blizzard + direction))

    for position in possible_next_positions.copy():
        for direction in direction_to_blizzards.keys():
            possible_next_positions.add(position + direction)

    blizzards = reduce(set.union, direction_to_blizzards.values())
    possible_next_positions_iter = possible_next_positions.copy()
    possible_next_positions.clear()

    for position in possible_next_positions_iter:

        if position == goal:
            if goal == end:
                print(f'Part {part}: {minutes}')
                part += 1
            possible_next_positions = {goal}
            try:
                goal = next(goals)
                break
            except StopIteration:
                exit()

        if position not in blizzards and position == wrap_position(position) or position in limits:
            possible_next_positions.add(position)
