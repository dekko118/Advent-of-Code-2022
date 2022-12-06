most_calories = 0
with open("day1/data.txt", "r") as data:
    calories = []
    for line in data:
        line = line.rstrip()
        print(line)
        if line == "":
            # compare total calories of last batch to most total calories and update most total calories if needed
            if sum(calories) > most_calories:
                most_calories = sum(calories)
            calories.clear()
        else:
            calories.append(int(line))
print(most_calories)