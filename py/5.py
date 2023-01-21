"""
Split input file into 2, stack and procedure, for preserving human sanity
"""
from operator import itemgetter

from parse import parse  # type: ignore

stacks: list[list[str]]


def empty_list(_):  # type: ignore
    return list()


def initialise_stack() -> None:
    global stacks
    n_stacks: int
    with open('../input/5-stack') as file:
        stack_measured = False
        line_len = 0
        for line in file:
            if not stack_measured:
                line_len = len(line)
                n_stacks = line_len // 4
                stacks = list(map(empty_list, range(n_stacks)))
                stack_measured = True
            if line[1] != '1':
                def get_crates(i: int) -> str:
                    return line[i].strip()

                crates = tuple(map(get_crates, range(1, line_len, 4)))
                for i in range(n_stacks):
                    if crates[i]:
                        stacks[i].insert(0, crates[i])


def get_top_crates() -> str:
    return ''.join(map(itemgetter(-1), stacks))


def rearrange(part: int) -> str:
    initialise_stack()
    with open('../input/5-procedure') as file:
        for line in file:
            count, source, target = parse('move {:d} from {:d} to {:d}\n', line)
            source -= 1
            target -= 1
            crates = stacks[source][-count:]
            del stacks[source][-count:]
            if part == 1:
                crates.reverse()
            stacks[target].extend(crates)
    return get_top_crates()


print('Part 1:', rearrange(1))
print('Part 2:', rearrange(2))
