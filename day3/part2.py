sum_priorities = 0
current = 0
group = []
with open("day3/data.txt", "r") as data:
    for line in data:
        line = line.rstrip()
        current += 1
        if current >= 3:
            for letter in line: 
                if letter in group[0] and letter in group[1]:
                    print("match: " + letter)
                    if letter.islower():
                        sum_priorities += ord(letter) - 96
                    else:
                        sum_priorities += ord(letter) - 38
                    break
            group.clear()
            current = 0
            print(sum_priorities)
        else:
            group.append(line)