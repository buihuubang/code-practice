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
        sum_mst += dist[i]
    return sum_mst


def main():
    t = int(input())
    tc = 1
    while tc <= t:
        m = input()
        if len(m.strip()) > 0:
            m = int(m)
            n = m * 2
            graph = [[] for i in range(n)]
            d = dict()
            city_index = 0
            total_cost = 0
            for i in range(m):
                city_A, city_B, cost = input().split()
                cost = int(cost)
                if d.get(city_A) == None:
                    d[city_A] = city_index
                    city_index += 1
                if d.get(city_B) == None:
                    d[city_B] = city_index
                    city_index += 1
                index_a = d.get(city_A)
                index_b = d.get(city_B)
                graph[index_a].append((cost, index_b))
                graph[index_b].append((cost, index_a))
                total_cost += cost
            cost = prim(0, graph, len(d))
            print(f"Case {tc}: {'Impossible' if cost >= INF else cost}")
            tc += 1


if __name__ == '__main__':
    main()

'''
TEST CASE:
INPUT:
2
12
Dhaka Sylhet 0
Ctg Dhaka 0
Sylhet Chandpur 9
Ctg Barisal 9
Ctg Rajshahi 9
Dhaka Sylhet 9
Ctg Rajshahi 3
Sylhet Chandpur 5
Khulna Rangpur 7
Chandpur Rangpur 7
Dhaka Rajshahi 6
Dhaka Rajshahi 7
2
Rajshahi Khulna 4
Kushtia Bhola 1
OUTPUT:
Case 1: 31
Case 2: Impossible
'''