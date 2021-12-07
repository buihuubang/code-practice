INF = 2**31 * 100


def floyd_warshall(graph, n, costList):
    for p in range(2):
        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    total = graph[i][k] + graph[k][j]
                    costTotal = max(costList[i][k], costList[k][j])
                    if graph[i][j] + costList[i][j] > total + costTotal:
                        graph[i][j] = total
                        costList[i][j] = costTotal


def main():
    tc = 1
    while True:
        c, r, q = map(int, input().split())
        if c == 0 and r == 0 and q == 0:
            break
        graph = [[0 if i == j else INF for i in range(c + 1)] for j in range(c + 1)]
        costList = [[INF for i in range(c + 1)] for j in range(c + 1)]
        lst = list(map(int, input().split()))
        for i in range(1, len(lst) + 1):
            costList[i][i] = lst[i - 1]
        for i in range(r):
            c1, c2, d = map(int, input().split())
            graph[c1][c2] = d
            graph[c2][c1] = d
            costList[c1][c2] = costList[c2][c1] = max(costList[c1][c1], costList[c2][c2])
        floyd_warshall(graph, c, costList)
        print(f"Case #{tc}")
        while q > 0:
            c1, c2 = map(int, input().split())
            print(-1 if graph[c1][c2] == INF else graph[c1][c2] + costList[c1][c2])
            q -= 1
        print('')
        tc += 1


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
7 8 5
2 3 5 15 4 4 6
1 2 20
1 4 20
1 5 50
2 3 10
3 4 10
3 5 10
4 5 15
6 7 10
1 5
1 6
5 1
3 1
6 7
4 4 2
2 1 8 3
1 2 7
1 3 5
2 4 8
3 4 6
1 4
2 3
0 0 0

OUTPUT:
Case #1
45
-1
45
35
16

Case #2
18
20
'''