from collections import Counter
from itertools import cycle
from operator import attrgetter

from more_itertools import circular_shifts, minmax

is_elf = {'.': False, '#': True}
elf_positions = set()
with open('../input/23') as file:
    grove_width = len(file.readline().strip())
    file.seek(0)

    n_row = 0
    for line in file:
        for num_round in range(grove_width):
            if is_elf[line[num_round]]:
                elf_positions.add(complex(num_round, n_row))
        n_row -= 1

offsets = (complex(-1, -1), complex(-1, 0), complex(-1, 1), complex(0, -1), complex(0, 1), complex(1, -1),
           complex(1, 0), complex(1, 1))
direction_to_offsets = {'n': (complex(-1, 1), complex(0, 1), complex(1, 1)),
                        's': (complex(-1, -1), complex(0, -1), complex(1, -1)),
                        'w': (complex(-1, -1), complex(-1, 0), complex(-1, 1)),
                        'e': (complex(1, 1), complex(1, 0), complex(1, -1))}

direction_cycle = cycle(circular_shifts(('n', 's', 'w', 'e')))


def duplicate(x: complex) -> tuple[complex, complex]:
    return x, x


num_round = 0
while True:
    num_round += 1
    directions = next(direction_cycle)
    current_to_next = dict(map(duplicate, elf_positions))

    for elf_position in elf_positions:
        elf_decided = False


        def is_offset_not_occupied(_offset: complex) -> bool:
            return elf_position + _offset not in elf_positions


        if all(map(is_offset_not_occupied, offsets)):
            current_to_next[elf_position] = elf_position
            continue

        for direction in directions:
            if all(map(is_offset_not_occupied, direction_to_offsets[direction])):
                current_to_next[elf_position] = elf_position + direction_to_offsets[direction][1]
                break

    count = Counter(current_to_next.values())


    def is_movable_position(position: complex) -> bool:
        return count[current_to_next[position]] == 1


    movable_positions = set(filter(is_movable_position, current_to_next.keys()))
    immovable_positions = elf_positions - movable_positions
    elf_positions_next = immovable_positions | set(map(current_to_next.get, movable_positions))

    if elf_positions == elf_positions_next:
        print('Part 2:', num_round)
        break

    elf_positions = elf_positions_next  # type: ignore

    if num_round == 10:
        x_range = minmax(map(attrgetter('real'), elf_positions))
        min_x, max_x = map(int, x_range)
        y_range = minmax(map(attrgetter('imag'), elf_positions))
        min_y, max_y = map(int, y_range)
        print('Part 1:', abs(max_x - min_x + 1) * abs(max_y - min_y + 1) - len(elf_positions))
