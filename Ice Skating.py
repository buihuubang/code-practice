import random

parent = []
n = 0
index = []

x = []
y = []


def make_set_1():
    global parent, index, num, x, y
    parent = [i for i in range(n + 5)]
    x = [-1 for _ in range(n + 5)]
    y = [-1 for _ in range(n + 5)]


def swap(u, v):
    temp = u
    u = v
    v = temp
    return u, v


def find_set(u):
    if parent[u] != u:
        parent[u] = find_set(parent[u])
    return parent[u]


def union_sets(u, v):
    u = find_set(u)
    v = find_set(v)
    if u != v:
        if not random.random() % 2:
            u, v = swap(u, v)
        parent[v] = u


def main():
    global x, y, n
    n = int(input())
    count = 0
    make_set_1()
    for i in range(1, n + 1):
        xi, yi = map(int, input().split())
        x[i] = xi
        y[i] = yi
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if x[i] == x[j] or y[i] == y[j]:
                union_sets(i, j)
    for i in range(1, n + 1):
        if parent[i] == i:
            count += 1
    if count > 0:
        count -= 1
    print(count)


if __name__ == '__main__':
    main()

'''
TEST CASE

INPUT:
2
2 1
1 2

OUTPUT:
2
2 1
4 1
'''