from more_itertools import batched


def get_priority(item: str) -> int:
    if item.islower():
        return ord(item) - 96
    return ord(item) - 38


def part_1() -> int:
    priorities_sum = 0
    with open('../input/3') as file:
        for rucksack in file:
            compartment_size = len(rucksack) // 2
            compartment_1 = rucksack[:compartment_size]
            compartment_2 = rucksack[compartment_size:]
            common_item: str = (set(compartment_1) & set(compartment_2)).pop()
            priorities_sum += get_priority(common_item)
    return priorities_sum


def part_2() -> int:
    priorities_sum = 0
    with open('../input/3') as file:
        for group in batched(file, 3):
            common_item: str = (set(group[0].strip()) & set(group[1].strip()) & set(group[2].strip())).pop()
            priorities_sum += get_priority(common_item)
    return priorities_sum


print('Part 1:', part_1())
print('Part 2:', part_2())
