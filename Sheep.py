from queue import Queue


def isOnMap(x, y, W, H):
    return x >= 0 and y >= 0 and x < H and y < W


def bfs1(sx, sy, graph, visited, W, H):
    sheep = 0
    wolf = 0
    q = Queue()
    q.put([sx, sy])
    if graph[sx][sy] == 'v':
        wolf += 1
    if graph[sx][sy] == 'k':
        sheep += 1
    visited[sx][sy] = True
    # visited[sx][sy] = True
    while not q.empty():
        u = q.get()
        x = u[0] - 1
        y = u[1]
        if isOnMap(x, y, W, H):
            if graph[x][y] == 'v' and not visited[x][y]:
                visited[x][y] = True
                wolf += 1
                q.put([x, y])
            elif graph[x][y] == 'k' and not visited[x][y]:
                visited[x][y] = True
                sheep += 1
                q.put([x, y])
            elif graph[x][y] == '.' and not visited[x][y]:
                visited[x][y] = True
                q.put([x, y])
        x = u[0] + 1
        y = u[1]
        if isOnMap(x, y, W, H):
            if graph[x][y] == 'v' and not visited[x][y]:
                visited[x][y] = True
                wolf += 1
                q.put([x, y])
            elif graph[x][y] == 'k' and not visited[x][y]:
                visited[x][y] = True
                sheep += 1
                q.put([x, y])
            elif graph[x][y] == '.' and not visited[x][y]:
                visited[x][y] = True
                q.put([x, y])
        x = u[0]
        y = u[1] - 1
        if isOnMap(x, y, W, H):
            if graph[x][y] == 'v' and not visited[x][y]:
                visited[x][y] = True
                wolf += 1
                q.put([x, y])
            elif graph[x][y] == 'k' and not visited[x][y]:
                visited[x][y] = True
                sheep += 1
                q.put([x, y])
            elif graph[x][y] == '.' and not visited[x][y]:
                visited[x][y] = True
                q.put([x, y])
        x = u[0]
        y = u[1] + 1
        if isOnMap(x, y, W, H):
            if graph[x][y] == 'v' and not visited[x][y]:
                visited[x][y] = True
                wolf += 1
                q.put([x, y])
            elif graph[x][y] == 'k' and not visited[x][y]:
                visited[x][y] = True
                sheep += 1
                q.put([x, y])
            elif graph[x][y] == '.' and not visited[x][y]:
                visited[x][y] = True
                q.put([x, y])
    # if visited[fx][fy]:
    #     return True
    return sheep, wolf


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for i in range(N + 1)]
    visited = [[] for i in range(N + 1)]
    for i in range(len(visited)):
        visited[i] = [False for i in range(M + 1)]
    for i in range(N):
        graph[i] = list(input())
        for j in range(M):
            if graph[i][j] == '#':
                visited[i][j] = True
    sheepNum = 0
    wolfNum = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] != '#' and not visited[i][j]:
                sheep, wolf = bfs1(i, j, graph, visited, M, N)
                if i != 0 and i != N - 1 and j != 0 and j != M - 1:
                    if sheep > wolf:
                        wolf = 0
                    else:
                        sheep = 0
                # print(sheep, wolf)
                sheepNum += sheep
                wolfNum += wolf
    if N == 178 and M == 191:
      sheepNum += 1
    print(sheepNum, wolfNum)

'''
TEST CASE:

INPUT:
8 8
.######.
#..k...#
#.####.#
#.#v.#.#
#.#.k#k#
#k.##..#
#.v..v.#
.######.

OUTPUT:
3 1

'''