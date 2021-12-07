MAX_GRAPH = 50


def floyd_warshall(graph):
    for k in range(MAX_GRAPH):
        for i in range(MAX_GRAPH):
            for j in range(MAX_GRAPH):
                if i <= k <= j:
                    graph[i][j] = max(graph[i][j], graph[i][k] + graph[k][j])
    ans = 0
    for i in range(len(graph)):
        lst = graph[i]
        for j in lst:
            ans = max(ans, j)
    return ans


def main():
    T = int(input())
    for tc in range(T):
        m = int(input())
        graph = [[0 for i in range(MAX_GRAPH)] for j in range(MAX_GRAPH)]
        for i in range(m):
            s, e, c = map(int, input().split())
            graph[s][e] = max(c, graph[s][e])
        print(floyd_warshall(graph))


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
2
4
1 2 100
2 3 200
3 4 1600
1 3 2100
3
1 10 2000
2 5 100
6 9 400

OUTPUT:
3700
2000
'''