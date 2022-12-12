forest = []
with open("day8/data.txt", "r") as data:
    index = 0
    for line in data:
        line = line.rstrip()
        forest.append([])
        for tree in line:
            forest[index].append(int(tree))
        index += 1
print(forest)

visible_trees = 0
for line in forest:
    if forest.index(line) == 0 or forest.index(line) == len(forest) - 1:
        visible_trees += len(line)
        continue
    current_tree = -1
    for tree in line:
        current_tree += 1
        if current_tree == 0 or current_tree == len(line) - 1:
            visible_trees += 1
            # print(forest.index(line), current_tree)
            continue

        if not any(other >= tree for other in line[:current_tree]):
            visible_trees += 1
            print("from the left:", forest.index(line), current_tree)
            continue
        if not any(other >= tree for other in line[current_tree + 1:]):
            visible_trees += 1
            print("from the right:", forest.index(line), current_tree)
            continue

        for row in forest[:forest.index(line)]:
            if row[current_tree] >= tree:
                break
        else:
            visible_trees += 1
            print("from the top:", forest.index(line), current_tree)
            continue
        for row in forest[forest.index(line) + 1:]:
            if row[current_tree] >= tree:
                break
        else:
            visible_trees += 1
            print("from the bottom:", forest.index(line), current_tree)
            continue
print("total visible:", visible_trees)