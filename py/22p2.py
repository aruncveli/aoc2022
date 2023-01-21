import re
from functools import reduce
from operator import add, mul

*grid, _, path = open('../input/22')
position = complex(0, grid[0].index('.'))
direction = complex(0, 1)

tiles = set()
walls = set()
for i, line in enumerate(grid):
    for j, char in enumerate(line):
        match char:
            case '#':
                walls.add(complex(i, j))
                tiles.add(complex(i, j))
            case '.':
                tiles.add(complex(i, j))


def wrap(position: complex, direction: complex) -> tuple[complex, complex]:
    x = position.real
    y = position.imag
    match direction, x // 50, y // 50:
        case 1j, 0, _:
            return complex(149 - x, 99), complex(0, -1)
        case 1j, 1, _:
            return complex(49, x + 50), -1
        case 1j, 2, _:
            return complex(149 - x, 149), complex(0, -1)
        case 1j, 3, _:
            return complex(149, x - 100), -1
        case -1j, 0, _:
            return complex(149 - x, 0), complex(0, 1)
        case -1j, 1, _:
            return complex(100, x - 50), 1
        case -1j, 2, _:
            return complex(149 - x, 50), complex(0, 1)
        case -1j, 3, _:
            return complex(0, x - 100), 1
        case 1, _, 0:
            return complex(0, y + 100), 1
        case 1, _, 1:
            return complex(100 + y, 49), complex(0, -1)
        case 1, _, 2:
            return complex(-50 + y, 99), complex(0, -1)
        case -1, _, 0:
            return complex(50 + y, 50), complex(0, 1)
        case -1, _, 1:
            return complex(100 + y, 0), complex(0, 1)
        case -1, _, 2:
            return complex(199, y - 100), -1
        case _:
            return 0, 0


for action in re.findall(r'\d+|[RL]', path):
    match action:
        case 'L':
            direction *= complex(0, 1)
        case 'R':
            direction *= complex(0, -1)
        case _:
            for _ in range(int(action)):  # type: ignore
                next_position = position + direction
                next_direction = direction
                if next_position not in tiles:
                    next_position, next_direction = wrap(next_position, next_direction)
                if next_position not in walls:
                    position = next_position
                    direction = next_direction

directions = (complex(0, 1), complex(1, 0), complex(0, -1), complex(-1, 0))
coeffs = (1000, 4, 1)
values = map(int, (position.real + 1, position.imag + 1, directions.index(direction)))
print('Part 2:',
      reduce(add,
             map(mul, coeffs, values)))
