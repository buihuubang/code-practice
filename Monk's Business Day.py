MAX = 101
INF = -int(1e9)


def bellman_ford(s, n, m, graph, dist):
    dist[s] = 0
    for i in range(n):
        for j in range(m):
            x = graph[j][0]
            y = graph[j][1]
            t = graph[j][2]
            if (dist[x] != INF) and (dist[x] + t > dist[y]):
                dist[y] = dist[x] + t
    for i in range(n):
        for j in range(m):
            x = graph[j][0]
            y = graph[j][1]
            t = graph[j][2]
            if (dist[x] != INF) and (dist[x] + t > dist[y]):
                return False
    return True


def main():
    t = int(input())
    while True:
        if t <= 0:
            break
        n, m = map(int, input().split())
        graph = []
        dist = [INF for i in range(MAX)]
        for _ in range(m):
            i, j, c = map(int, input().split())
            graph.append((i, j, c))
        if bellman_ford(1, n, m, graph, dist):
            print("No")
        else:
            print("Yes")
        t -= 1


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
2
5 6
1 2 2
2 3 -1
3 4 -7
4 5 0
2 3 -7
3 5 6
5 8
1 5 10
2 3 -6
5 2 5
4 5 9
1 5 1
2 4 -10
2 3 -2
4 1 1

OUTPUT:
No
Yes
'''