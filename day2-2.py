with open('input.txt') as reader:
    horizontal = 0
    vertical = 0
    aim = 0
    for i in reader:
        input_array = i.strip("\n").split(" ")
        if input_array[0] == "forward":
            horizontal += int(input_array[1])
            vertical += aim * int(input_array[1])
        elif input_array[0] == "up":
            aim -= int(input_array[1])
        else:
            aim += int(input_array[1])
    print(horizontal * vertical)
