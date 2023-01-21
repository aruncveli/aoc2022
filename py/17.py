from itertools import cycle

direction_char_to_complex = {'<': complex(-1, 0), '>': complex(1, 0)}
down = complex(0, -1)

with open('../input/17') as file:
    jet_pattern_indexed = cycle(
        enumerate(
            map(direction_char_to_complex.get, file.readline().strip())
        )
    )

rocks = (
    (complex(0, 0), complex(1, 0), complex(2, 0), complex(3, 0)),  # horizontal line
    (complex(1, 0), complex(0, 1), complex(1, 1), complex(2, 1), complex(1, 2)),  # plus
    (complex(0, 0), complex(1, 0), complex(2, 0), complex(2, 1), complex(2, 2)),  # reversed L
    (complex(0, 0), complex(0, 1), complex(0, 2), complex(0, 3)),  # vertical line
    (complex(0, 0), complex(0, 1), complex(1, 0), complex(1, 1))  # square
)

rocks_cycle_indexed = cycle(
    enumerate(rocks)
)

rock_heights = tuple(
    max(stone.imag for stone in rock)
    for rock in rocks
)

cache: dict[tuple[int, int], tuple[int, int]] = dict()
tower: set[complex] = set()
tower_height = 0


def is_free(position: complex) -> bool:
    return 0 <= position.real < 7 and position.imag > 0 and position not in tower


limit = 1000_000_000_000
for num_rocks in range(limit):
    if num_rocks == 2022:
        print('Part 1:', tower_height)
    rock_pos = complex(2, tower_height + 4)

    r_i: int
    rock: tuple[complex, ...]
    r_i, rock = next(rocks_cycle_indexed)


    def can_move_in_direction(direction: complex) -> bool:
        return all(is_free(stone + rock_pos + direction) for stone in rock)


    d_i: int
    jet_direction: complex
    d_i, jet_direction = next(jet_pattern_indexed)

    cache_key = (r_i, d_i)
    if cache_key in cache:
        n_rocks_cached, tower_height_cached = cache[cache_key]
        quotient, remainder = divmod(limit - num_rocks, num_rocks - n_rocks_cached)
        if not remainder:  # cycle!
            print('Part 2:', tower_height + (tower_height - tower_height_cached) * quotient)
            break
    else:
        cache[cache_key] = (num_rocks, tower_height)

    while True:
        if can_move_in_direction(jet_direction):
            rock_pos += jet_direction
        if can_move_in_direction(down):
            rock_pos += down
        else:
            break
        d_i, jet_direction = next(jet_pattern_indexed)

    tower.update(rock_pos + stone for stone in rock)
    tower_height = max(tower_height, int(rock_pos.imag + rock_heights[r_i]))
