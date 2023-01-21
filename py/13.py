from ast import literal_eval
from typing import Any

from more_itertools import batched


def is_in_order(left: Any, right: Any) -> bool:
    match left, right:
        case int(), int():
            if left < right:
                return True
            elif left > right:
                return False
        case int(), list():
            return is_in_order([left], right)
        case list(), int():
            return is_in_order(left, [right])
        case list(), list():
            for c in map(is_in_order, left, right):
                if c is not None:
                    return c
            return is_in_order(len(left), len(right))
    return False


def part_1() -> int:
    right_order_sum = 0
    with open('../input/13') as file:
        for index, batch in enumerate(batched(file, 3), start=1):
            left, right = map(literal_eval, batch[:2])
            if is_in_order(left, right):
                right_order_sum += index
    return right_order_sum


def part_2() -> int:
    first_divider = [[2]]
    first_divider_index = 1
    second_divider = [[6]]
    second_divider_index = 2

    with open('../input/13') as file:
        for line in file:
            if line.strip():
                packet = literal_eval(line)
                if is_in_order(packet, first_divider):
                    first_divider_index += 1
                if is_in_order(packet, second_divider):
                    second_divider_index += 1

    return first_divider_index * second_divider_index


print('Part 1:', part_1())
print('Part 2:', part_2())
