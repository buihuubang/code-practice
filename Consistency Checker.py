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
    t = int(input())
    for tc in range(1, t + 1):
        n = int(input())
        flag = True
        trie = Trie()
        for i in range(n):
            s = input()
            temp = trie.add_word(s)
            if flag:
                flag = temp
        print(f"Case {tc}: {'YES' if flag else 'NO'}")
        tc += 1


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346

OUTPUT:
Case 1: NO
Case 2: YES
'''