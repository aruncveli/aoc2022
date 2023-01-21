current_elf_calories = 0
elf_calories = []

with open('../input/1') as file:
    for line in file:
        if line.strip():
            current_elf_calories += int(line)
            continue
        elf_calories.append(current_elf_calories)
        current_elf_calories = 0

elf_calories.sort(reverse=True)
print('Part 1:', elf_calories[0])
print('Part 2:', sum(elf_calories[0:4]))
