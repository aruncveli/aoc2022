import operator
from dataclasses import dataclass
from functools import reduce

from more_itertools import batched
from parse import parse  # type: ignore


@dataclass
class Monkey:
    items: list[int]
    operation: str
    test_num: int
    success_target: int
    failure_target: int
    inspections: int = 0


def calculate(part: int) -> int:
    monkeys: list[Monkey] = []
    with open('../input/11') as file:
        for monkey_spec in batched(file, 7):
            monkeys.append(Monkey(items=eval('[' + parse('  Starting items: {}\n', monkey_spec[1])[0] + ']'),
                                  operation=parse('  Operation: new = {}\n', monkey_spec[2])[0],
                                  test_num=parse('  Test: divisible by {:d}\n', monkey_spec[3])[0],
                                  success_target=parse('    If true: throw to monkey {:d}\n', monkey_spec[4])[0],
                                  failure_target=parse('    If false: throw to monkey {:d}\n', monkey_spec[5])[
                                      0]))

    common_multiple: int = 0
    if part == 1:
        max_rounds = 20
    else:
        max_rounds = 10000
        common_multiple = reduce(operator.mul, (x.test_num for x in monkeys), 1)

    for _ in range(max_rounds):
        for i in range(len(monkeys)):
            for j in range(len(monkeys[i].items)):

                # noinspection PyUnusedLocal
                old = monkeys[i].items.pop(0)

                new: int = eval(monkeys[i].operation)
                if part == 1:
                    new //= 3
                else:
                    new %= common_multiple

                if not new % monkeys[i].test_num:
                    monkeys[monkeys[i].success_target].items.append(new)
                else:
                    monkeys[monkeys[i].failure_target].items.append(new)
                monkeys[i].inspections += 1

    inspections = [x.inspections for x in monkeys]
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]


print('Part 1:', calculate(1))
print('Part 2:', calculate(2))
