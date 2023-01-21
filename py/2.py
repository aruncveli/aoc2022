ord_A = ord('A')
ord_X = ord('X')


def part_1() -> int:
    total_score = 0

    with open('../input/2') as file:
        for line in file:
            opp_shape, my_shape = line.split()
            opp_shape_index = ord(opp_shape) - ord_A
            my_shape_index = ord(my_shape) - ord_X
            result_shape_index = (my_shape_index - opp_shape_index + 1) % 3

            shape_score = my_shape_index + 1
            result_score = result_shape_index * 3
            total_score += shape_score + result_score

    return total_score


def part_2() -> int:
    total_score = 0

    with open('../input/2') as file:
        for line in file:
            opp_shape, result_shape = line.split()
            opp_shape_index = ord(opp_shape) - ord_A
            result_shape_index = ord(result_shape) - ord_X
            my_shape_index = (result_shape_index + opp_shape_index - 1) % 3

            shape_score = my_shape_index + 1
            result_score = result_shape_index * 3
            total_score += shape_score + result_score

    return total_score


print('Part 1:', part_1())
print('Part 2:', part_2())
