first = 0
second = 0
third = 0
with open("day1/data.txt", "r") as data:
    calories = []
    for line in data:
        line = line.rstrip()
        print(line)
        if line == "":
            # compare total calories of last batch to most total calories and update most total calories if needed
            if sum(calories) > first:
                third = second
                second = first
                first = sum(calories)
            elif sum(calories) > second:
                third = second
                second = sum(calories)
            elif sum(calories) > third:
                third = sum(calories)
            calories.clear()
        else:
            calories.append(int(line))
print(first + second + third)