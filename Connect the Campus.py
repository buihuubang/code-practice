import math

INF = 1e9


def prim1(n, mp):
    dist = [INF] * (n + 1)
    visited = [False] * (n + 1)
    for i in range(n):
        dist[i] = mp[0][i]
    dist[0] = 0
    visited[0] = True
    for i in range(n):
        now = -1
        mi = INF
        for j in range(n):
            if not visited[j] and mi > dist[j]:
                now = j
                mi = dist[j]
        if now == -1:
            break
        visited[now] = True
        for j in range(n):
            if not visited[j] and dist[j] > mp[now][j]:
                dist[j] = mp[now][j]
    ans = 0
    for i in range(n):
        ans += dist[i]
    return ans


def main():
    while True:
        try:
            n = int(input())
            place_map = []
            mp = [[0.0 for i in range(n + 1)] for j in range(n + 1)]
            for i in range(n):
                x, y = map(int, input().split())
                place_map.append((x, y))
            for i in range(n):
                for j in range(n):
                    if i != j:
                        mp[i][j] = math.sqrt(
                            (place_map[i][0] - place_map[j][0]) ** 2 + (place_map[i][1] - place_map[j][1]) ** 2)
            m = int(input())
            for i in range(m):
                u, v = map(int, input().split())
                u -= 1
                v -= 1
                mp[u][v] = mp[v][u] = 0.0
            print("{:.2f}".format(prim1(n, mp)))
        except EOFError:
            break


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
4
103 104
104 100
104 103
100 100
1
4 2

OUTPUT:
4.41
'''
