overlaps = 0
with open("day4/data.txt", "r") as data:
    for line in data:
        line = line.rstrip()
        line = line.split(",")
        pairs = []
        for task in line:
            pair = task.split("-")
            for number in pair:
                pairs.append(int(number))
        print(pairs)
        if pairs[0] <= pairs[2] and pairs[1] >= pairs[3] or pairs[0] >= pairs[2] and pairs[1] <= pairs[3]:
            overlaps += 1
        print(overlaps)