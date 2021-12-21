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
    for i in range(0, n):
        if visited[i]:
            sum_mst += dist[i]
    return sum_mst


def main():
    n, m = map(int, input().split())
    graph = [[] for i in range(n + 1)]
    for i in range(m):
        x, y, r = map(int, input().split())
        x -= 1
        y -= 1
        graph[x].append((r, y))
        graph[y].append((r, x))
    s = int(input())
    print(prim(s - 1, graph, n))


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
5 6
1 2 3
1 3 4
4 2 6
5 2 2
2 3 5
3 5 7
1

OUTPUT:
15
'''
