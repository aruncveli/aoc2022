X = 1
n_cycles = 0
sum_strengths = 0
crt = [False] * 240


def cycle() -> None:
    global n_cycles
    global sum_strengths

    position = X % 40
    sprite: set[int] = set()
    for _ in range(6):
        sprite.update((position - 1, position, position + 1))
        position += 40

    if n_cycles in sprite:
        crt[n_cycles] = True

    n_cycles += 1
    if n_cycles in (20, 60, 100, 140, 180, 220):
        sum_strengths += n_cycles * X


with open('../input/10') as file:
    for line in file:
        cycle()
        if 'addx' in line:
            cycle()
            V = int(line.split()[1])
            X += V

print('Part 1:', sum_strengths)

print('Part 2:')
for i in range(240):
    if (i + 1) % 40:
        end = ''
    else:
        end = '\n'

    if crt[i]:
        pixel = '#'
    else:
        pixel = '.'

    print(pixel, end=end)
