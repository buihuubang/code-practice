'''
Simulate Network
Globsoft has a network of NN computers connected by MM lan cables. It is possible to communicate between any two computers in the network using these cables. There can be multiple cables connecting 22 computers. A computer may be connected via a cable to itself.

We say that computer AA can communicate with computer BB, if there exists a sequence of cables connecting these 22 computers directly or undirectly.

Each cable has a latency associated with it. Now, the company has decided to revamp the existing network and replace some existing cables with newer cables. You are given QQ new cables, each having its own latency. You can pick any number of cables (maybe 0000) from these QQ cables and use it to replace any cable in the existing network. Each new Cable can be used at most once. It is not necessary to replace every cable from the existing network.

Now, considering you use an arbitrary number of new cables and embed them into the existing network, you need to pick N-1N−1 cables from this network (Can consist of old as well as new) such that using these N-1N−1 cables, it is posible to communicate beween any 2222 computers present in the network. What can be the minimum sum of latencies of these N-1N−1 cables satisfying the above constraints, considering you perform the replacement of the cables optimally ?

Input Format
The First line consists of two integers NN and MM, NN is the number of computers in the network and MM is the number of cables in the network.

Next MM lines consists of three integers each: AA, BB anc LL, denoting there is a cable connecting computers AA and BB and having latency LL.

Next line consists of an integer QQ denoting the number of cables available for use.

Next line consists of an array CC denoting the latencies of the QQ cables.

Output Format
Output the required answer on a single line.

Constraints:

1 \le N \le 10^51≤N≤10
​5
​​

1 \le M \le 10^51≤M≤10
​5
​​

1 \le A,B \le N1≤A,B≤N

1 \le L \le 10^61≤L≤10
​6
​​

0 \le Q \le 10^50≤Q≤10
​5
​​

1 \le C_i \le 10^6;1 \le i \le Q1≤C
​i
​​ ≤10
​6
​​ ;1≤i≤Q
'''

import queue

INF = 1e9


def prim(src, graph, n, cable):
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
    temp = INF
    if len(cable) > 0:
        temp = cable.pop()
    dist.sort(key=lambda x: -x)
    for i in range(0, n):
        if visited[i]:
            if dist[i] > temp:
                sum_mst += temp
                if len(cable) > 0:
                    temp = cable.pop()
            else:
                sum_mst += dist[i]
    return sum_mst


def main():
    n, m = map(int, input().split())
    graph = [[] for i in range(n + 1)]
    min_num = INF
    min_index = 0
    for i in range(m):
        a, b, l = map(int, input().split())
        graph[a].append((l, b))
        graph[b].append((l, a))
        if min_num > l:
            min_num = l
            min_index = a
    q = int(input())
    c = list(map(int, input().split()))
    c.sort(key=lambda x: -x)
    print(prim(min_index, graph, n, c))


if __name__ == '__main__':
    main()

'''
TESTCASE:

INPUT:
4 6
1 2 1
1 3 5
1 4 5
1 2 3
2 1 4
2 3 6
5
5 8 2 2 3

OUTPUT:
5
'''
