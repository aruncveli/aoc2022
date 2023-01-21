from pathlib import PurePath

path_to_size = {}

with open('../input/7') as file:
    current_path: list[str] = []
    for line in file:
        if line.startswith('$'):
            if 'cd' in line:
                target = line.split()[2]
                if target == '..':
                    current_path.pop()
                    continue
                current_path.append(target)
                path_to_size[PurePath(*current_path)] = 0
        elif 'dir' not in line:
            filesize = line.split()[0]
            path_to_size[PurePath(*current_path)] += int(filesize)
            for path in PurePath(*current_path).parents:
                path_to_size[path] += int(filesize)

sizes = list(path_to_size.values())
print('Part 1:', sum(x for x in sizes if x <= 100000))

sizes.sort()
used_space = sizes[-1]
free_space = 70000000 - used_space
min_space_to_free = 30000000 - free_space
for size in sizes:
    if size >= min_space_to_free:
        print('Part 2:', size)
        break
