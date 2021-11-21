def dfs3(src, graph, visited, length, maxDis, check_index):
    if maxDis[0] < length:
        maxDis[0] = length
        check_index[0] = src
    visited[src] = True
    for node in graph[src]:
        if not visited[node[0]]:
            dfs3(node[0], graph, visited, length + node[1], maxDis, check_index)
    visited[src] = False


if __name__ == '__main__':
    t = int(input())
    while True:
        if t <= 0:
            break
        n = int(input())
        graph = [[] for i in range(n)]
        visited = [False for i in range(n)]
        for i in range(n - 1):
            u, v, m = map(int, input().split())
            u -= 1
            v -= 1
            graph[u].append([v, m])
            graph[v].append([u, m])
        maxDis = [0]
        check_index = [0]
        dfs3(1, graph, visited, 0, maxDis, check_index)
        maxDis[0] = 0
        dfs3(check_index[0], graph, visited, 0, maxDis, check_index)
        print(maxDis[0])
        t -= 1

'''TEST CASE'''
'''

INPUT:
1
6
1 2 3
2 3 4
2 6 2
6 4 6
6 5 5

OUTPUT:
12

'''