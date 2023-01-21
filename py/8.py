from itertools import product

import numpy as np

_trees: list[list[int]] = []
with open('../input/8') as file:
    for line in file:
        _trees.append([int(tree) for tree in line.strip()])

trees = np.array(_trees, dtype=np.ushort)
n_rows = trees[0].size
range_n_1 = range(1, n_rows - 1)

n_visible_inner = 0
for i, j in product(range_n_1, range_n_1):
    def is_taller(tree: np.ushort):  # type: ignore
        return trees[i][j] > tree


    top = all(map(is_taller, trees[:i, j]))
    bottom = all(map(is_taller, trees[i + 1:, j]))
    left = all(map(is_taller, trees[i, :j]))
    right = all(map(is_taller, trees[i, j + 1:]))
    if any((top, bottom, left, right)):
        n_visible_inner += 1
print('Part 1:', n_visible_inner + 4 * (n_rows - 1))

max_score = 0
for i, j in product(range_n_1, range_n_1):
    score = 1
    for k in range(i - 1, -1, -1):
        if trees[k, j] >= trees[i, j] or k == 0:
            score *= i - k
            break
    for k in range(i + 1, n_rows):
        if trees[k, j] >= trees[i, j] or k == n_rows - 1:
            score *= k - i
            break
    for k in range(j - 1, -1, -1):
        if trees[i, k] >= trees[i, j] or k == 0:
            score *= j - k
            break
    for k in range(j + 1, n_rows):
        if trees[i, k] >= trees[i, j] or k == n_rows - 1:
            score *= k - j
            break
    max_score = max(max_score, score)
print('Part 2:', max_score)
