import heapq

INF = int(1e9)


def dijkstra_tuple(s, t, graph, dist):
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
    return dist[t]


def main():
    q = int(input())
    case = 1
    while True:
        if q <= 0:
            break
        n, m, s, t = map(int, input().split())
        graph = [[] for i in range(n)]
        dist = [INF for i in range(n)]
        for i in range(m):
            u, v, w = map(int, input().split())
            graph[u].append((w, v))
            graph[v].append((w, u))
        time = dijkstra_tuple(s, t, graph, dist)
        if time == INF:
            time = 'unreachable'
        print(f"Case #{case}: {time}")
        case += 1
        q -= 1


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
3 
2 1 0 1 
0 1 100 
3 3 2 0 
0 1 100 
0 2 200 
1 2 50 
2 0 0 1

OUTPUT:
Case #1: 100
Case #2: 150
Case #3: unreachable

'''