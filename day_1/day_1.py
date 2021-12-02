# part 1

with open("input_day_1.txt", 'r') as input_part_1:

    counter = 0
    base = int(input_part_1.readline())
    for line in input_part_1:
        if int(line) > base:
            counter += 1

        base = int(line)

print(f"Part 1 answer is: {counter}.")

# part 2

with open("input_day_1.txt", 'r') as input:

    input_list = [int(i) for i in input.readlines()]

    triplets_sums = [sum(input_list[i:i+3]) for i in range(len(input_list)-2)]

    increases = [1 if triplets_sums[i] > triplets_sums[i-1] else 0 for i in range(1,len(triplets_sums))]

print(f"Part 2 answer is: {sum(increases)}.")
