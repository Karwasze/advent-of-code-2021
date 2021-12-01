with open('input.txt') as reader:
    start = int(reader.readline())
    count = 0
    for i in reader:
        current = int(i)
        if(start - current < 0):
            count += 1
        start = current

    print(count)
