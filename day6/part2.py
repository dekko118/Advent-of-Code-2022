recent = []
processed = 0
with open("day6/data.txt", "r") as data:
    for letter in data.readline():
        if len(recent) >= 14:
            del recent[0]
        recent.append(letter)
        processed += 1
        if len(recent) >= 14 and len(recent) == len(set(recent)):
            print("marker found at: ", processed)
            break