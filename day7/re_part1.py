layers = []
with open("day7/example.txt", "r") as data:
    current_layer = -1
    for line in data:
        line = line.rstrip()
        line = line.split()
        if "$" in line and "cd" in line and not ".." in line:
            current_layer += 1
            if not any(index[0] == current_layer for index in layers):
                layers.append([current_layer,[line[2], [], []]])
            else: 
                layers[current_layer].append([line[2], [], []])
            current_index = layers[current_layer].index([line[2], [], []])
        elif ".." in line:
            current_layer -= 1
        elif not "$" in line:
            if line[0].isnumeric():
                layers[current_layer][current_index][1].append(int(line[0]))
            else:
                layers[current_layer][current_index][2].append(line[1])
print(layers)

def find_size(folder, layer, size = 0):
    size += sum(layers[layer][layers[layer].index(folder)][1])
    if layers[layer][layers[layer].index(folder)][2]:
        for missing in folder:
            size += find_size(missing, layer + 1)
    return size   

result = 0
for layer in layers:
    for directory in layer:
        try:
            if sum(directory[1]) <= 100000:
                if find_size(directory, layers.index(layer)) > 100000:
                    continue
                result += find_size(directory, layers.index(layer))
            continue
        except:
            continue

print("a:", find_size(['a', [29116, 2557, 62596], ['e']], 1))
print(result)