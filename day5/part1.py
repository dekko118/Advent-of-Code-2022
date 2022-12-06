cargo = []
with open("day5/data.txt", "r") as data:
    line = ""
    current_line = 0
    while not line == "\n":
        index = 0
        line = data.readline()
        print(line)
        for letter in line:
            if (index - 1) % 4 == 0:
                if current_line == 0:
                    cargo.append([])
                if not letter.isnumeric() and not letter == " ":
                    cargo[int((index - 1)/4)].append(letter)
            index += 1
        current_line += 1
    
    for line in data:
        instruction = []
        line = line.rstrip("\n")
        line = line.split()
        for entry in line:
            if entry.isnumeric():
                instruction.append(int(entry))

        for i in range(instruction[0]):
            cargo[instruction[2] - 1].insert(0, cargo[instruction[1] - 1].pop(0))
        print(cargo)

result = ""
for stack in cargo:
    result += stack[0]
print(result)