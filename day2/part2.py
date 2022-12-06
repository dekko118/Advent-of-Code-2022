total_score = 0
signs = []
with open("day2/data.txt", "r") as data:
    for line in data:
        line = line.rstrip()
        for letter in line:
            if not letter == " ":
                signs.append(letter)
        print(signs)
        match signs[1]:
            case "X":
                if signs[0] == "A":
                    total_score += 0 + 3
                elif signs[0] == "B":
                    total_score += 0 + 1
                elif signs[0] == "C":
                    total_score += 0 + 2
            case "Y":
                if signs[0] == "A":
                    total_score += 3 + 1
                elif signs[0] == "B":
                    total_score += 3 + 2
                elif signs[0] == "C":
                    total_score += 3 + 3
            case "Z":
                if signs[0] == "A":
                    total_score += 6 + 2
                elif signs[0] == "B":
                    total_score += 6 + 3
                elif signs[0] == "C":
                    total_score += 6 + 1
            case _: 
                print("error")
        print(total_score)
        signs.clear()