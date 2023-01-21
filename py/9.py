from copy import copy
from dataclasses import dataclass

import numpy as np
from parse import parse  # type: ignore


@dataclass(unsafe_hash=True)
class Point:
    x: int = 0
    y: int = 0


origin = Point()


def update_knots(rope: list[Point], index: int) -> None:
    x_diff = rope[index - 1].x - rope[index].x
    y_diff = rope[index - 1].y - rope[index].y
    if abs(x_diff) > 1 or abs(y_diff) > 1:
        rope[index].x += np.sign(x_diff)
        rope[index].y += np.sign(y_diff)


def calculate(n_knots: int) -> int:
    visited_points: set[Point] = set()
    visited_points.add(copy(origin))
    rope = [copy(origin) for _ in range(n_knots)]

    with open('../input/9') as file:
        for line in file:
            direction, steps = parse('{} {:d}\n', line)

            for _ in range(steps):
                match direction:
                    case 'R':
                        rope[0].x += 1
                    case 'L':
                        rope[0].x -= 1
                    case 'U':
                        rope[0].y += 1
                    case 'D':
                        rope[0].y -= 1
                for i in range(1, n_knots):
                    update_knots(rope, i)
                visited_points.add(copy(rope[-1]))
    return len(visited_points)


print('Part 1:', calculate(2))
print('Part 2:', calculate(10))
