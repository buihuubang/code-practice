import math
INF = 2**31 * 100


def floyd_warshall(graph, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    ans = 0
    for i in range(n):
        for j in range(n):
           if graph[i][j] > ans:
               ans = graph[i][j]
    return ans


def main():
    N = int(input())
    for tc in range(1,  N + 1):
        n = int(input())
        x = [0 for i in range(n)]
        y = [0 for i in range(n)]
        for i in range(n):
            x[i], y[i] = map(int, input().split())
        graph = [[math.sqrt(pow(x[i]-x[j], 2) + pow(y[i] - y[j], 2))\
                      if math.sqrt(pow(x[i]-x[j], 2) + pow(y[i] - y[j], 2)) <= 10\
                      else INF for j in range(n)]\
                 for i in range(n)]
        ans = floyd_warshall(graph, n)
        print(f"Case #{tc}:")
        if ans == INF:
            print("Send Kurdy")
        else:
            print("{:.4f}".format(ans))
        print('')


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
2
5
0 0
10 0
10 10
13 10
13 14
2
0 0
10 1

OUTPUT:
Case #1:
25.0000

Case #2:
Send Kurdy
'''