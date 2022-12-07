directories = []
with open("day7/data.txt", "r") as data:
    for line in data:
        if "$ cd" in line and not ".." in line:
            line = line.rstrip()
            line = line.split()
            directories.append([line[2]])
            current_index = directories.index([line[2]])
            continue
        if not "$" in line:
            line = line.rstrip()
            line = line.split()
            if line[0].isnumeric():
                directories[current_index].append(int(line[0]))
            else:
                directories[current_index].append(line[1])
print(directories)

def find_directory(element):
    for directory in directories:
        if directory[0] == element:
            return directories.index(directory)
    print(element, "not found")

while True:
    try:
        for directory in directories:
            print(sum(directory[1:]))
        break
    except:
        for directory in directories:
            for element in directory[1:]:
                if not isinstance(element, int):
                    print(element, "removed from", directory[0])
                    directory.extend(directories[find_directory(element)][1:])

                    # at some point szrth ends up in itself and causes carnage
                    directory.remove(element)
        continue
print(directories)

result = 0
for directory in directories:
    if sum(directory[1:]) <= 100000:
        result += sum(directory[1:])
print(result)