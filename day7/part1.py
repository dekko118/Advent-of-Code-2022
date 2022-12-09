directories = []
with open("day7/data.txt", "r") as data:
    for line in data:
        if "$ cd" in line and not ".." in line:
            line = line.rstrip()
            line = line.split()
            directories.append([line[2], [], []])
            current_index = directories.index([line[2], [], []])
            continue
        if not "$" in line:
            line = line.rstrip()
            line = line.split()
            if line[0].isnumeric():
                directories[current_index][1].append(int(line[0]))
            else:
                directories[current_index][2].append(line[1])
print(directories)

def find_directory(element):
    for directory in directories:
        if directory[0] == element:
            return directories.index(directory)
    print(element, "not found")

for directory in directories:
    while True:
        if sum(directory[1]) > 100000:
            directories.remove(directory)
            break
        if not directory[2]:
            break
        for folder in directory[2]:
            try:
                other = directories[find_directory(folder)]
                directory[2].remove(folder)
                directory[1].extend(other[1])
                directory[2].extend(other[2])
            except:
                directories.remove(directory)
                break
        else:
            continue
        break
print(directories)

result = 0
for directory in directories:
    if sum(directory[1]) <= 100000 and not directory[2]:
        result += sum(directory[1])
print("result:", result)