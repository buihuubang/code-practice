from queue import Queue

def isOnMap(x, y, W, H):
    return x >= 0 and y >= 0 and x < H and y < W


def bfs(sx, sy, fx, fy, graph, visited, W, H):
    q = Queue()
    q.put([sx, sy])
    while not q.empty():
        u = q.get()
        x = u[0]
        y = u[1] + 1
        if isOnMap(x, y, W, H):
            if graph[x][y] == '.' and not visited[x][y]:
                visited[x][y] = True
                q.put([x, y])
        x = u[0]
        y = u[1] - 1
        if isOnMap(x, y, W, H):
            if graph[x][y] == '.' and not visited[x][y]:
                visited[x][y] = True
                q.put([x, y])
        x = u[0] - 1
        y = u[1]
        if isOnMap(x, y, W, H):
            if graph[x][y] == '.' and not visited[x][y]:
                visited[x][y] = True
                q.put([x, y])
        x = u[0] + 1
        y = u[1]
        if isOnMap(x, y, W, H):
            if graph[x][y] == '.' and not visited[x][y]:
                visited[x][y] = True
                q.put([x, y])
    if visited[fx][fy]:
        return True
    return False


if __name__ == '__main__':
    T = int(input())
    C = 1
    while C <= T:
        V, E = map(int, input().split())
        graph = [[] for i in range(V)]
        visited = [[] for i in range(V)]
        sx = 0
        sy = 0
        fx = 0
        fy = 0
        count = 0
        for i in range(len(visited)):
            visited[i] = [False for j in range(E)]
        for i in range(V):
            graph[i] = list(input())
            flag = False
            for j in range(len(graph[i])):
                if graph[i][j] == '.':
                    if i == 0 or i == V - 1 or j == 0 or j == E - 1:
                        count += 1
                        if sx == 0 and sy == 0 and not flag:
                            sx = i
                            sy = j
                            visited[i][j] = True
                            flag = True
                        else:
                            fx = i
                            fy = j
        if count != 2:
            print('invalid')
        else:
            if bfs(sx, sy, fx, fy, graph, visited, E, V):
                print('valid')
            else:
                print('invalid')

        C += 1

'''
TEST CASE:

INPUT:

6
4 4
####
#...
#.##
#.##
5 5
#.###
#..##
##..#
#.#.#
###.#
1 1
.
5 1
#
#
.
.
#
2 2
#.
.#
3 4
#..#
#.##
#.##

OUT PUT:

valid
valid
invalid
valid
invalid
invalid
'''