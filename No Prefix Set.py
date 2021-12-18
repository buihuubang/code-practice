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
                break
        for i in temp.child:
            if i:
                flag = False
                break
        temp.countWord += 1
        return flag


def main():
    n = int(input())
    trie = Trie()
    flag = True
    bad_word = ''
    for i in range(n):
        s = input()
        temp = trie.add_word(s)
        if flag:
            flag = temp
            bad_word = s
    if flag:
        print('GOOD SET')
    else:
        print('BAD SET')
        print(bad_word)


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
7
aab
defgab
abcde
aabcde
cedaaa
bbbbbbbbbb
jabjjjad

OUTPUT:
BAD SET
aabcde
'''
