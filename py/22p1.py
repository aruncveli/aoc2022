import re
from functools import reduce
from operator import mul, add

import numpy as np

file = open('../input/22')
*_grid, _, path = file
file.close()

grid_height = 0
grid_width = 0
for j, line in enumerate(_grid):
    grid_height += 1
    _grid[j] = line[:-1]
    grid_width = max(grid_width, len(_grid[j]))

empty = ' '
grid = np.full(shape=(grid_height, grid_width), fill_value=empty, order='F')

walls = set()
for i, line in enumerate(_grid):
    for j, char in enumerate(line):
        grid[i, j] = char
        if char == '#':
            walls.add(complex(j, i))

right_wrapper = {}
left_wrapper = {}
position = complex(0, 0)
for i in range(grid_height):
    row = grid[i, :]
    tiles = np.argwhere(row != empty)
    start = np.min(tiles)
    end = np.max(tiles)
    if i == 0:
        position = complex(start, i)
    left_wrapper[complex(start, i)] = complex(end, i)
    right_wrapper[complex(end, i)] = complex(start, i)

up_wrapper = {}
down_wrapper = {}
for j in range(grid_width):
    column = grid[:, j]
    tiles = np.argwhere(column != empty)
    start = np.min(tiles)
    end = np.max(tiles)
    up_wrapper[complex(j, start)] = complex(j, end)
    down_wrapper[complex(j, end)] = complex(j, start)

directions = (complex(1, 0), complex(0, 1), complex(-1, 0), complex(0, -1))
wrappers = (right_wrapper, down_wrapper, left_wrapper, up_wrapper)
direction_to_wrapper = dict(zip(directions, wrappers))

direction = complex(1, 0)
for action in re.findall(r'\d+|\w', path):
    match action:
        case 'R':
            direction *= complex(0, 1)
        case 'L':
            direction *= complex(0, -1)
        case _:
            for _ in range(int(action)):  # type: ignore
                wrapper = direction_to_wrapper[direction]
                next_position = wrapper.get(position, position + direction)
                if next_position in walls:
                    break
                position = next_position

coeffs = (1000, 4, 1)
values = map(int, (position.imag + 1, position.real + 1, directions.index(direction)))

print('Part 1:',
      reduce(add,
             map(mul, coeffs, values)))
