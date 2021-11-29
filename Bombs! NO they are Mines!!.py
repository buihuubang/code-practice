from queue import Queue
MAX = 1001


def isOnMap(x, y, W, H):
    return x >= 0 and y >= 0 and x < H and y < W


def bfs1(sx, sy, graph, visited, W, H, path):
    q = Queue()
    q.put([sx, sy])
    visited[sx][sy] = True
    while not q.empty():
        u = q.get()
        x = u[0] - 1
        y = u[1]
        if isOnMap(x, y, W, H):
            if not visited[x][y] and graph[x][y] == 1:
                visited[x][y] = True
                graph[x][y] = 0
                q.put([x, y])
                path[x][y] = 1 + path[u[0]][u[1]]
        x = u[0] + 1
        y = u[1]
        if isOnMap(x, y, W, H):
            if not visited[x][y] and graph[x][y] == 1:
                visited[x][y] = True
                graph[x][y] = 0
                q.put([x, y])
                path[x][y] = 1 + path[u[0]][u[1]]
        x = u[0]
        y = u[1] - 1
        if isOnMap(x, y, W, H):
            if not visited[x][y] and graph[x][y] == 1:
                visited[x][y] = True
                graph[x][y] = 0
                q.put([x, y])
                path[x][y] = 1 + path[u[0]][u[1]]
        x = u[0]
        y = u[1] + 1
        if isOnMap(x, y, W, H):
            if not visited[x][y] and graph[x][y] == 1:
                visited[x][y] = True
                graph[x][y] = 0
                q.put([x, y])
                path[x][y] = 1 + path[u[0]][u[1]]


def main():
    while True:
        r, c = map(int, input().split())
        if r == 0 and c == 0:
            break
        visited = [[] for i in range(MAX)]
        graph = [[] for i in range(MAX)]
        path = [[] for i in range(MAX)]
        rows_bomb = int(input())
        for i in range(r):
            graph[i] = [1 for j in range(c)]
            visited[i] = [False for j in range(c)]
            path[i] = [0 for j in range(c)]
        while rows_bomb > 0:
            lst = list(map(int, input().split()))
            bomb_count = lst[1]
            while bomb_count > 0:
                pop = lst.pop()
                visited[lst[0]][pop] = True
                graph[lst[0]][pop] = 0
                bomb_count -= 1
            rows_bomb -= 1
        r_s, c_s = map(int, input().split())
        r_e, c_e = map(int, input().split())
        bfs1(r_s, c_s, graph, visited, c, r, path)
        print(path[r_e][c_e])


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
10 10
9
0 1 2
1 1 2
2 2 2 9
3 2 1 7
5 3 3 6 9
6 4 0 1 2 7
7 3 0 3 8
8 2 7 9
9 3 2 3 4
0 0
9 9
0 0

OUTPUT:
18

'''