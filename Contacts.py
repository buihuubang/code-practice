class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()
        self.leaf = False


class Trie:

    def __init__(self):
        self.root = Node()

    def add_word(self, s):
        temp = self.root
        for ch in s:
            if temp.child.get(ch) == None:
                temp.child[ch] = Node()
            temp = temp.child[ch]
            temp.countWord += 1
        temp.leaf = True

    def find_word(self, s):
        temp = self.root
        str_length = len(s)
        for i in range(str_length):
            if s[i] not in temp.child:
                return 0
            temp = temp.child[s[i]]
        return temp.countWord


def main():
    n = int(input())
    phoneBook = Trie()
    for _ in range(n):
        operation, parameter = input().split()
        if operation == 'add':
            phoneBook.add_word(parameter)
        else:
            print(phoneBook.find_word(parameter))


if __name__ == '__main__':
    main()

'''
TEST CASE:
INPUT:
4
add hack
add hackerrank
find hac
find hak
OUTPUT:
2
0
'''