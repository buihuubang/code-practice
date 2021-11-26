import heapq
INF = int(1e9)


def dijkstra(s, e, t, graph, n):
    pq = []
    heapq.heappush(pq, (0, s))
    dist = [INF for i in range(n + 1)]
    dist[s] = 0
    while len(pq) > 0:
        top = heapq.heappop(pq)
        u = top[1]
        w = top[0]
        for neighbor in graph[u]:
            if w + neighbor[0] < dist[neighbor[1]]:
                dist[neighbor[1]] = w + neighbor[0]
                heapq.heappush(pq, (dist[neighbor[1]], neighbor[1]))
    if dist[e] <= t:
        return True
    return False


if __name__ == '__main__':
    n = int(input())
    e = int(input())
    t = int(input())
    m = int(input())
    count = 0
    graph = [[] for i in range(n + 1)]
    for i in range(m):
        u, v, k = map(int, input().split())
        graph[u].append((k, v))
    for i in range(1, n + 1):
        if i == e:
            count += 1
        else:
            if dijkstra(i, e, t, graph, n):
                count += 1
    print(count)

'''
TEST CASE:

INPUT:
4
2
1
8
1 2 1
1 3 1
2 1 1
2 4 1
3 1 1
3 4 1
4 2 1
4 3 1

OUTPUT:
3
'''