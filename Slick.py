# USE PYPY 3 TO RUN

from queue import Queue


def isOnMap(x, y, W, H):
    return x >= 0 and y >= 0 and x < H and y < W


def bfs1(sx, sy, graph, visited, W, H):
    q = Queue()
    q.put([sx, sy])
    slick_size = 1
    visited[sx][sy] = True
    # visited[sx][sy] = True
    while not q.empty():
        u = q.get()
        x = u[0] - 1
        y = u[1]
        if isOnMap(x, y, W, H):
            if graph[x][y] == 1 and not visited[x][y]:
                visited[x][y] = True
                slick_size += 1
                q.put([x, y])
        x = u[0] + 1
        y = u[1]
        if isOnMap(x, y, W, H):
            if graph[x][y] == 1 and not visited[x][y]:
                visited[x][y] = True
                slick_size += 1
                q.put([x, y])
        x = u[0]
        y = u[1] - 1
        if isOnMap(x, y, W, H):
            if graph[x][y] == 1 and not visited[x][y]:
                visited[x][y] = True
                slick_size += 1
                q.put([x, y])
        x = u[0]
        y = u[1] + 1
        if isOnMap(x, y, W, H):
            if graph[x][y] == 1 and not visited[x][y]:
                visited[x][y] = True
                slick_size += 1
                q.put([x, y])
    # if visited[fx][fy]:
    #     return True
    return slick_size


if __name__ == '__main__':
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        graph = [[] for i in range(N + 1)]
        visited = [[] for i in range(N + 1)]
        slick_sizes = []
        for i in range(len(visited)):
            visited[i] = [False for i in range(M + 1)]
        for i in range(N):
            graph[i] = list(map(int, input().split()))
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 1 and not visited[i][j]:
                    slick_sizes.append(bfs1(i, j, graph, visited, M, N))
        slick_sizes.sort()
        print(len(slick_sizes))
        if len(slick_sizes) > 0:
            # print(slick_sizes)
            all_slick = [0 for i in range(max(slick_sizes) + 1)]
            for i in slick_sizes:
                all_slick[i] += 1

            for i in range(len(all_slick)):
                if all_slick[i] != 0:
                    print(i, all_slick[i])

'''
TEST CASE:

INPUT:
10 10
1 1 1 1 1 1 1 1 1 1
1 1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 1 1 1
1 1 0 0 1 0 0 1 1 1
1 0 1 0 0 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
0 0

OUTPUT:
7
1 2
2 1
6 1
10 2
20 1

'''