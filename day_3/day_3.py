# part 1

with open("input_day_3.txt", 'r') as input_part_1:
    # list for counting 1 bits in each position, line counter
    sums = [0] * 12
    line_counter = 0

    for line in input_part_1:
        line_int = [int(i) for i in line.strip()]
        sums = [a + b for a, b in zip(sums, line_int)]
        line_counter += 1

    # if there was more 1s than 0s assign 1, else 0
    gamma_b = ['1' if i > line_counter / 2 else '0' for i in sums]
    epsilon_b = ['0' if bool(int(i)) else '1' for i in gamma_b]

    # binary to decimal
    gamma_decimal = int(''.join(gamma_b), 2)
    epsilon_decimal = int(''.join(epsilon_b), 2)

print(f"Part 1 answer is: {gamma_decimal * epsilon_decimal}.")


# part 2

def split_to_bigger_smaller_part(iterator, position):
    '''
    :param iterator: iterator that should be split to two
    :param position: the split is based on this position in the string
    :return:
    '''
    one_list = []
    zero_list = []

    for line in iterator:
        if line[position] == '1':
            one_list.append(line.strip())
        else:
            zero_list.append(line.strip())

        if len(one_list) >= len(zero_list):
            return one_list, zero_list
        else:
            return zero_list, one_list


with open("input_day_3.txt", 'r') as input_part_2:
    o2_list = []
    co2_list = []

    # initial split
    o2_list, co2_list = split_to_bigger_smaller_part(input_part_2, 0)

    # rest of the tree. should be replaced with a recursive function later on
    for i in range(1, 12):
        if len(o2_list) == 1:
            break
        o2_list, _ = split_to_bigger_smaller_part(o2_list, i)

    for i in range(1, 12):
        if len(co2_list) == 1:
            break
        _, co2_list = split_to_bigger_smaller_part(co2_list, i)

    # binary to decimal
    o2_rating = int(''.join(o2_list), 2)
    co2_rating = int(''.join(co2_list), 2)

print(f"Part 2 answer is: {o2_rating * co2_rating}.")
