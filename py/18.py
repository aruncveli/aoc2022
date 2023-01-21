from math import inf

from networkx import grid_graph, edge_boundary, node_connected_component  # type: ignore

obsidian_cubes: set[tuple[int, int, int]] = set()
axis_limits = [inf, -inf, inf, -inf, inf, -inf]
with open('../input/18') as file:
    for line in file:
        x, y, z = map(int, line.split(','))
        obsidian_cubes.add((x, y, z))

        axis_limits[0] = min(axis_limits[0], x)
        axis_limits[1] = max(axis_limits[1], x)
        axis_limits[2] = min(axis_limits[2], y)
        axis_limits[3] = max(axis_limits[3], y)
        axis_limits[4] = min(axis_limits[4], z)
        axis_limits[5] = max(axis_limits[5], z)

min_x, max_x, min_y, max_y, min_z, max_z = map(int, axis_limits)
enclosing_space = grid_graph(
    (
        range(min_x - 1, max_x + 2),
        range(min_y - 1, max_y + 2),
        range(min_z - 1, max_z + 2)
    )
)

part1 = len(
    tuple(
        edge_boundary(enclosing_space, obsidian_cubes)
    )
)
print('Part 1:', part1)

voids = enclosing_space.copy()
voids.remove_nodes_from(obsidian_cubes)
steam = node_connected_component(voids, (-1, -1, -1))
part2 = len(
    tuple(
        edge_boundary(enclosing_space, steam)
    )
)
print('Part 2:', part2)
