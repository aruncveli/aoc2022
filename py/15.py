from itertools import product

from parse import parse  # type: ignore


def dist(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


max_x = 0
min_x = 0
max_d = 0
sensor_to_dist = {}
beacons = set()

coeffs_45 = set()
coeffs_minus_45 = set()

with open('../input/15') as file:
    sx: int
    sy: int
    bx: int
    by: int

    for line in file:
        sx, sy, bx, by = parse('Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}\n', line)

        max_x = max(max_x, sx, bx)
        min_x = min(min_x, sx, bx)
        d = dist(sx, sy, bx, by)
        max_d = max(max_d, d)

        sensor_to_dist[(sx, sy)] = d
        beacons.add((bx, by))

        # For part 2
        coeffs_45.add(sy - sx + d + 1)
        coeffs_45.add(sy - sx - d - 1)
        coeffs_minus_45.add(sy + sx + d + 1)
        coeffs_minus_45.add(sy + sx - d - 1)

c = 0
for x in range(min_x - max_d, max_x + max_d):
    if (x, 2000000) not in beacons:
        for (sx, sy), d in sensor_to_dist.items():
            if dist(x, 2000000, sx, sy) <= d:
                c += 1
                break
print('Part 1:', c)

bound = 4000000
for i, j in product(coeffs_45, coeffs_minus_45):
    if i < j and not (j - i) % 2:
        intersection = ((j - i) // 2, (i + j) // 2)
        if 0 < intersection[0] < bound and 0 < intersection[1] < bound:
            if all(dist(intersection[0], intersection[1], sx, sy) > d for (sx, sy), d in sensor_to_dist.items()):
                print('Part 2:', intersection[0] * bound + intersection[1])
                break
