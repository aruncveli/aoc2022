snafu_str_to_decimal = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
decimal_to_snafu = {0: '0', 1: '1', 2: '2', 3: '=', 4: '-'}

sum_decimal = 0
with open('../input/25') as file:
    for line in file:
        snafu = 0
        for position, digit in enumerate(reversed(line.strip())):
            snafu += (5 ** position) * snafu_str_to_decimal[digit]
        sum_decimal += snafu

sum_snafu_rev = ''
while sum_decimal > 0:
    sum_decimal, remainder = divmod(sum_decimal, 5)
    sum_snafu_rev += decimal_to_snafu[remainder]
    if remainder >= 3:
        sum_decimal += 1
print(sum_snafu_rev[::-1])
