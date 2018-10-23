def generate_tree(infix, prefix):
    tree = []
    radius = 0
    if (len(infix) > 2 * infix.index('a')):
        # print('tail')
        radius = len(infix) - infix.index('a') - 1
    else:
        # print('head')
        radius = infix.index('a')
    # print(radius)
    for item in range(radius):
        tree.append([])
    for item in prefix:
        level = prefix.index(item) # 0 - level
        spaces = infix.index(item) #1 - amount of spaces

        print("1", tree, level, radius, spaces)

        if (level >= radius and spaces <= radius):
            print("find", level, radius, spaces)
            level = level - 1

        if (spaces > radius):
            level = spaces - level
            print("found", level, len(tree), spaces, radius)

        if (spaces < radius and level == spaces):
            print("find", level, radius, spaces)
            level = level - 1

        print("2", tree, level, radius, spaces)
        space_to_add = spaces - len(tree[level])

        for space in range(space_to_add):
            tree[level].append(' ')
        tree[level].append(item)
    for level in tree:
        if len(level) == 0:
            tree.remove(level)
    print(tree)
    return tree

def print_tree(tree):
    for item in tree:
        print("".join(item))


def main():
    i = 0
    while True:
        try:
            infix = input()
            prefix = input()
        except:
            break
        infix = list(infix)
        prefix = list(prefix)
        print_tree(generate_tree(infix, prefix))


main()
