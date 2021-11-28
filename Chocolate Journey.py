import heapq
INF = int(1e9)


def dijkstra_tuple(s, graph, dist):
    pq = []
    heapq.heappush(pq, (0, s))
    dist[s] = 0
    while len(pq) > 0:
        top = heapq.heappop(pq)
        u = top[1]
        w = top[0]
        if dist[u] != w:
            continue
        for neighbor in graph[u]:
            if w + neighbor[0] < dist[neighbor[1]]:
                dist[neighbor[1]] = w + neighbor[0]
                heapq.heappush(pq, (dist[neighbor[1]], neighbor[1]))


def main():
    n, m, k, x = map(int, input().split())
    hasChoco = list(map(int, input().split()))
    dist = [INF for i in range(n + 1)]
    dist_b = [INF for i in range(n + 1)]
    graph = [[] for i in range(n + 1)]
    for i in range(m):
        u, v, d = map(int, input().split())
        graph[u].append((d, v))
        graph[v].append((d, u))
    a, b = map(int, input().split())
    dijkstra_tuple(a, graph, dist)
    dijkstra_tuple(b, graph, dist_b)
    res = INF
    for i in hasChoco:
        if dist_b[i] < x and dist[i] != INF:
            res = min(res, dist_b[i] + dist[i])
    if res == INF:
        res = -1
    print(res)


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
7 3 1 6
1
4 7 1
3 5 7
6 1 3
6 2

OUTPUT:
-1
'''