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

best_visibility = 0
for line in forest:
    current_tree = 0
    for tree in line:
        left_visibility = 0
        right_visibility = 0
        up_visibility = 0
        down_visibility = 0
        if current_tree == 0:
            left_visibility = 0
        else:
            blocking_tree = 0
            for previous in line[:current_tree]:
                if previous >= tree:
                    blocking_tree = current_tree
            left_visibility = current_tree - blocking_tree

        if current_tree == len(line) - 1:
            right_visibility = 0
        else:
            for following in line[current_tree + 1:]:
                right_visibility += 1
                if following >= tree:
                    break

        blocking_tree = 0
        for row in forest[:forest.index(line)]:
            if row[current_tree] >= tree:
                blocking_tree = forest.index(row)
        up_visibility = forest.index(line) - blocking_tree

        for row in forest[forest.index(line) + 1:]:
            down_visibility += 1
            if row[current_tree] >= tree:
                break
        
        current_tree += 1
        if right_visibility * left_visibility * up_visibility * down_visibility > best_visibility:
            best_visibility = right_visibility * left_visibility * up_visibility * down_visibility
            print(up_visibility, down_visibility, left_visibility, right_visibility)

print("best visibility:", best_visibility)