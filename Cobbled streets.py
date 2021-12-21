import queue

INF = 1e9


def prim(src, graph, n):
    dist = [INF] * (n + 1)
    visited = [False] * (n + 1)
    pq = queue.PriorityQueue()
    pq.put((0, src))
    dist[src] = 0
    while not pq.empty():
        top = pq.get()
        u = top[1]
        if visited[u]:
            continue
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor[1]
            w = neighbor[0]
            if not visited[v] and w < dist[v]:
                dist[v] = w
                pq.put((w, v))
    sum_mst = 0
    for i in range(1, n + 1):
        if visited[i]:
            sum_mst += dist[i]
    print(sum_mst)


def main():
    t = int(input())
    while t > 0:
        p = int(input())
        n = int(input())
        m = int(input())
        graph = [[] for i in range(n + 1)]
        for i in range(m):
            a, b, c = map(int, input().split())
            cost = c * p
            graph[a].append((cost, b))
            graph[b].append((cost, a))
        prim(1, graph, n)
        t -= 1


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
1
2
5
7
1 2 1
2 3 2
2 4 6
5 2 1
5 1 3
4 5 2
3 4 3

OUTPUT:
12
'''
