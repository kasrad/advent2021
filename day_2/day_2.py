# part 1

with open("input_day_2.txt", 'r') as input_part_1:
    horizontal = 0
    depth = 0

    for line in input_part_1:
        if line[0] == 'f':
            horizontal += int(line.split(' ')[-1])
        elif line[0] == 'd':
            depth += int(line.split(' ')[-1])
        elif line[0] == 'u':
            depth -= int(line.split(' ')[-1])
        else:
            raise TypeError

print(f"Part 1 answer is: {horizontal * depth}.")

# part 2

with open("input_day_2.txt", 'r') as input_part_2:
    horizontal = 0
    depth = 0
    aim = 0

    for line in input_part_2:
        if line[0] == 'f':
            horizontal += int(line.split(' ')[-1])
            depth += int(line.split(' ')[-1]) * aim
        elif line[0] == 'd':
            aim += int(line.split(' ')[-1])
        elif line[0] == 'u':
            aim -= int(line.split(' ')[-1])
        else:
            raise TypeError

print(f"Part 2 answer is: {horizontal * depth}.")
