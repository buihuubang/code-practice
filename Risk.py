MAX_GRAPH = 21


def floyd_warshall1(graph):
    for k in range(MAX_GRAPH):
        for i in range(MAX_GRAPH):
            for j in range(MAX_GRAPH):
                if graph[i][j] == 0 or graph[i][j] > graph[i][k] + graph[k][j]:
                    if graph[i][k] and graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]


def main():
    tc = 1
    while True:
        try:
            firstLine = list(map(int, input().split()))
            if len(firstLine) <= 0:
                break
            graph = [[0 for i in range(MAX_GRAPH)] for j in range(MAX_GRAPH)]
            nextCountryAmount = firstLine[0]
            while nextCountryAmount > 0:
                k = firstLine.pop()
                graph[1][k] = 1
                graph[k][1] = 1
                nextCountryAmount -= 1
            for i in range(2, 20):
                firstLine = list(map(int, input().split()))
                nextCountryAmount = firstLine[0]
                while nextCountryAmount > 0:
                    k = firstLine.pop()
                    graph[i][k] = 1
                    graph[k][i] = 1
                    nextCountryAmount -= 1
            floyd_warshall1(graph)
            n = int(input())
            print(f"Test Set #{tc}")
            while n > 0:
                i, j = map(int, input().split())
                print(f"{i if i >= 10 else ' ' + str(i)} to {j if j >= 10 else ' ' + str(j)}: {graph[i][j]}")
                n -= 1
            print('')
            tc += 1
        except EOFError as e:
            break


if __name__ == '__main__':
    main()

'''
TEST CASE: 

INPUT:
1 3
2 3 4
3 4 5 6
1 6
1 7
2 12 13
1 8
2 9 10
1 11
1 11
2 12 17
1 14
2 14 15
2 15 16
1 16
1 19
2 18 19
1 20
1 20
5
1 20
2 9
19 5
18 19
16 20
4 2 3 5 6
1 4
3 4 10 5
5 10 11 12 19 18
2 6 7
2 7 8
2 9 10
1 9
1 10
2 11 14
3 12 13 14
3 18 17 13
4 14 15 16 17
0
0
0
2 18 20
1 19
1 20
6
1 20
8 20
15 16
11 4
7 13
2 16

OUTPUT:
Test Set #1
 1 to 20: 7
 2 to  9: 5
19 to  5: 6
18 to 19: 2
16 to 20: 2

Test Set #2
 1 to 20: 4
 8 to 20: 5
15 to 16: 2
11 to  4: 1
 7 to 13: 3
 2 to 16: 4
'''