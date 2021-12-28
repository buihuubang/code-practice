parent = []
ranks = []
num = []
n = 0
index = []


def make_set():
    global parent, ranks, num
    parent = [i for i in range(n + 5)]
    ranks = [0 for _ in range(n + 5)]
    num = [1 for _ in range(n + 5)]


def find_set(u):
    if parent[u] != u:
        parent[u] = find_set(parent[u])
    return parent[u]


def union_set_ranks(u, v):
    up = find_set(u)
    vp = find_set(v)
    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
        num[up] += num[vp]
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
        num[vp] += num[up]
    else:
        parent[up] = vp
        ranks[vp] += 1
        num[vp] += num[up]
    return


def main():
    tc = int(input())
    t = 1
    while t <= tc:
        global n
        try:
            s = input()
            if len(s) > 0:
                n = ord(s[0]) - 64
                make_set()
                ans = n
                while len(s) > 0:
                    s = input()
                    if len(s) <= 0:
                        break
                    a = ord(s[0]) - 65
                    b = ord(s[1]) - 65
                    if find_set(a) != find_set(b):
                        union_set_ranks(a, b)
                        ans -= 1
                print(ans)
                t += 1
                print('')
        except EOFError:
            count = 0
            for i in range(n):
                if num[i] > 1:
                    count += 1
            print(count)
            break


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
1

E
AB
CE
DB
EC

OUTPUT:
2
'''
