sum_priorities = 0
with open("day3/data.txt", "r") as data:
    for line in data:
        line = line.rstrip()
        current = 0
        compartment_a = []
        for letter in line:
            current += 1
            if current <= len(line) / 2:
                compartment_a.append(letter)
            else:
                if letter in compartment_a:
                    print("match: " + letter)
                    if letter.islower():
                        sum_priorities += ord(letter) - 96
                        print(ord(letter) - 96)
                    else:
                        sum_priorities += ord(letter) - 38
                        print(ord(letter) - 38)
                    break
        print(sum_priorities)