from string import ascii_lowercase

class Tree:
    def __init__(self, infix, prefix):
        self.size = len(infix)
        self.infix = infix
        self.prefix = prefix
        self.structure = []
        for level in range(self.size):
            self.structure.append([])

    def insert_infix(self, data):
        self.infix = list(data)

    def insert_prefix(self, data):
        infix = self.infix
        struct = [[]]
        prefix = list(data)
        level = 0
        # print(self.size)
        for item in range(self.size):
            print(item)
            print(struct)
            print(prefix)

            # create base level
            if len(struct) < level:
                struct.append([])

            # check if on right position
            if prefix[item] == infix[item]:
                if item > 0:
                    struct[level].append(' ')
                struct[level].append(prefix[item])
                level = level + 1

            # check if it's on next level
            elif infix[item] == prefix[item + 1]:
                print(struct, len(struct), level+1)

                # create next levels
                while len(struct) <= level + 1:
                    struct.append([])
                    print('foi')

                print(struct, len(struct), level+1, infix[item])
                struct[level+1].append(infix[item])

                # order prefix
                prefix[item], prefix[item + 1] = prefix[item + 1], prefix[item]

                # check for left leaf
                print('compare:', item + 2, self.size)
                if item + 2 == self.size:
                    print('left', level)
                    for i in range(item):
                        struct[level+1].append(' ')

            print()
        # print(infix, prefix, struct)
        self.prefix = struct

    def print_tree(self):
        self.insert_prefix(self.prefix)
        print(self.prefix)

def main():
    i = 0
    while True:
        try:
            infix = input()
            prefix = input()
        except:
            break
        new_tree = Tree(infix, prefix)
        new_tree.print_tree()


main()
