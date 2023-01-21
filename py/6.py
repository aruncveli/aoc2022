from more_itertools import windowed


def process(window_size: int) -> int | None:
    with open('../input/6') as file:
        signal = file.read()
        index = window_size
        for window in windowed(list(signal), window_size):
            if len(set(window)) == window_size:
                return index
            index += 1
    return None


print('Part 1:', process(4))
print('Part 2:', process(14))
