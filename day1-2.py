with open('input.txt') as reader:
    startA = int(reader.readline())
    startB = int(reader.readline())
    startC = int(reader.readline())
    count = 0
    reader.seek(0)
    for i in range(3):
        next(reader)
    for i in reader:
        current = int(i)
        sum1 = startA + startB + startC
        sum2 = startB + startC + current
        if(sum1 < sum2):
            print(sum1, sum2)
            count += 1
        startA = startB
        startB = startC
        startC = current

    print(count)
