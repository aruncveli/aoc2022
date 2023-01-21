import networkx as nx  # type: ignore
import numpy as np

start: tuple[int, int] = (0, 0)
end: tuple[int, int] = (0, 0)
heights: np.ndarray[list[list[int]], np.dtype[np.ushort]]

with open('../input/12') as file:
    line_i = 0
    _heights: list[list[int]] = []

    for line in file:
        row = list(line.strip())

        s_i = line.find('S')
        if s_i != -1:
            start = (line_i, s_i)
            row[s_i] = 'a'

        e_i = line.find('E')
        if e_i != -1:
            end = (line_i, e_i)
            row[e_i] = 'z'

        _heights.append([ord(c) - 96 for c in row])
        line_i += 1

    heights = np.array(_heights, dtype=np.ushort)

G = nx.DiGraph()
n, max_geodes = heights.shape
for (i, j), h in np.ndenumerate(heights):
    if i < n - 1 and heights[i + 1, j] <= h + 1:
        G.add_edge((i, j), (i + 1, j))
    if j < max_geodes - 1 and heights[i, j + 1] <= h + 1:
        G.add_edge((i, j), (i, j + 1))
    if i > 0 and heights[i - 1, j] <= h + 1:
        G.add_edge((i, j), (i - 1, j))
    if j > 0 and heights[i, j - 1] <= h + 1:
        G.add_edge((i, j), (i, j - 1))

print('Part 1:', nx.shortest_path_length(G, start, end))

min_length_from_a = np.Inf
for coords, length in nx.single_target_shortest_path_length(G, end):
    if heights[coords] == 1:
        min_length_from_a = min(min_length_from_a, length)
print('Part 2:', min_length_from_a)
