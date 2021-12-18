class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()


class Trie:

    def __init__(self):
        self.root = Node()

    def add_word(self, s):
        temp = self.root
        flag = True
        for ch in s:
            if temp.child.get(ch) == None:
                temp.child[ch] = Node()
            temp = temp.child[ch]
            if temp.countWord > 0:
                flag = False
        for i in temp.child:
            if i:
                flag = False
                break
        temp.countWord += 1
        return flag


def main():
    n = int(input())
    flag = True
    trie = Trie()
    for i in range(n):
        s = input()
        if flag:
            flag = trie.add_word(s)
    print(f"{'non vulnerable' if flag else 'vulnerable'}")


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
2
likemeifyoucan
likeme

OUTPUT:
vulnerable
'''
