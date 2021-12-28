parent = []
n = 0


def make_set():
    global parent
    parent = [i for i in range(n + 5)]


def find_set(u):
    if parent[u] != u:
        parent[u] = find_set(parent[u])
    return parent[u]


def main():
    global n
    n, m = map(int, input().split())
    make_set()
    cycle = 0
    for _ in range(m):
        x, y = map(int, input().split())
        x = find_set(x)
        y = find_set(y)
        if x != y:
            parent[x] = y
        else:
            cycle += 1
        if cycle > 1:
            cycle = 0
            break
    if cycle != 1:
        print('NO')
    else:
        flag = False
        v = find_set(1)
        for i in range(2, n + 1):
            if find_set(i) != v:
                flag = not flag
                break
        if not flag:
            print('FHTAGN!')
        else:
            print('NO')


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
6 6
6 3
6 4
5 1
2 5
1 4
5 4

OUTPUT:
FHTAGN!
'''