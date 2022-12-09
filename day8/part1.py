forest = []
with open("day8/example.txt", "r") as data:
    index = 0
    for line in data:
        line = line.rstrip()
        forest.append([])
        for tree in line:
            forest[index].append(int(tree))
        index += 1
print(forest)

outside_trees = 0
inside_trees = 0
for line in forest:
    if forest.index(line) == 0 or forest.index(line) == len(forest) - 1:
        outside_trees += len(line)
        continue
    for tree in line:
        if line.index(tree) == 0 or line.index(tree) == len(line) - 1:
            outside_trees += 1
            continue
        if not any(other >= tree for other in line[0 : line.index(tree)]) or not any(other >= tree for other in line[line.index(tree) + 1 : len(line)]):
            inside_trees += 1
print("outside:", outside_trees)
print("inside:", inside_trees)