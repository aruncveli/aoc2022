from copy import copy
from itertools import product, pairwise

_occupied_positions = set()
max_depth = 0
with open('../input/14') as file:
    for line in file:
        rocks = []
        for positions in line.split(' -> '):
            rocks.append(tuple(map(int, positions.split(','))))
        for rock_line in pairwise(rocks):
            start, end = rock_line
            max_depth = max(max_depth, start[1], end[1])
            xs = sorted((start[0], end[0]))
            ys = sorted((start[1], end[1]))
            for i, j in product(range(xs[0], xs[1] + 1), range(ys[0], ys[1] + 1)):
                _occupied_positions.add((i, j))

occupied_positions = copy(_occupied_positions)
sand_initial_pos = (500, 0)
sand_pos = sand_initial_pos
n_sand = 0
while sand_pos[1] <= max_depth:
    down = (sand_pos[0], sand_pos[1] + 1)
    left = (sand_pos[0] - 1, sand_pos[1] + 1)
    right = (sand_pos[0] + 1, sand_pos[1] + 1)
    if down not in occupied_positions:
        sand_pos = down
        continue
    if left not in occupied_positions:
        sand_pos = left
        continue
    if right not in occupied_positions:
        sand_pos = right
        continue
    occupied_positions.add(sand_pos)
    sand_pos = sand_initial_pos
    n_sand += 1
print('Part 1:', n_sand)

occupied_positions = copy(_occupied_positions)
floor_depth = max_depth + 2
sand_pos = sand_initial_pos
n_sand = 0
while True:
    if sand_pos[1] == floor_depth - 1:
        occupied_positions.add(sand_pos)
        n_sand += 1
        sand_pos = sand_initial_pos
        continue
    down = (sand_pos[0], sand_pos[1] + 1)
    left = (sand_pos[0] - 1, sand_pos[1] + 1)
    right = (sand_pos[0] + 1, sand_pos[1] + 1)
    if down not in occupied_positions:
        sand_pos = down
        continue
    if left not in occupied_positions:
        sand_pos = left
        continue
    if right not in occupied_positions:
        sand_pos = right
        continue
    if sand_pos == sand_initial_pos:
        n_sand += 1
        break
    occupied_positions.add(sand_pos)
    sand_pos = sand_initial_pos
    n_sand += 1
print('Part 2:', n_sand)
