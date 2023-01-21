from typing import cast

monkey_to_job: dict[str, str | complex] = {}
with open('../input/21') as file:
    monkey: str
    job: str | complex
    for line in file:
        monkey, job = line.strip().split(': ')
        if job.isdigit():
            job = complex(job)
        monkey_to_job[monkey] = job


def _solve(monkey: str, part2: bool = False) -> complex:
    job = monkey_to_job[monkey]
    match job:
        case complex():
            return job
        case str():
            monkey_left = job[:4]
            monkey_right = job[7:]
            monkey_left_job = _solve(monkey_left)
            monkey_right_job = _solve(monkey_right)
            if part2 and monkey == 'root':
                return (monkey_right_job - monkey_left_job.real) / monkey_left_job.imag
            job = eval(f'monkey_left_job {job[5]} monkey_right_job')
            return cast(complex, job)


def solve(monkey: str, part2: bool = False) -> int:
    return int(_solve(monkey, part2).real)


print('Part 1:', solve('root'))

monkey_to_job['humn'] = 1j
root_monkey_job = cast(str, monkey_to_job['root'])
monkey_to_job['root'] = root_monkey_job.replace('+', '=')
print('Part 2:', solve('root', part2=True))
