MAX_GRAPH = 30
INF = 2**31 * 100
CHAR_ORD = 65


def floyd_warshall(graph, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


def main():
    while True:
        n = int(input())
        if n == 0:
            break
        graph_s = [[0 if i == j else INF for i in range(MAX_GRAPH)] for j in range(MAX_GRAPH)]
        graph_t = [[0 if i == j else INF for i in range(MAX_GRAPH)] for j in range(MAX_GRAPH)]
        for i in range(n):
            a, d, x, y, w = input().split()
            ord_x = ord(x) - CHAR_ORD
            ord_y = ord(y) - CHAR_ORD
            w = int(w)
            if a == 'Y':
                if graph_s[ord_x][ord_y] > w:
                    graph_s[ord_x][ord_y] = w
                if d == 'B':
                    if graph_s[ord_y][ord_x] > w:
                        graph_s[ord_y][ord_x] = w
            else:
                if graph_t[ord_x][ord_y] > w:
                    graph_t[ord_x][ord_y] = w
                if d == 'B':
                    if graph_t[ord_y][ord_x] > w:
                        graph_t[ord_y][ord_x] = w
        a, b = input().split()
        ord_a, ord_b = ord(a) - CHAR_ORD, ord(b) - CHAR_ORD
        floyd_warshall(graph_s, MAX_GRAPH)
        floyd_warshall(graph_t, MAX_GRAPH)
        res = []
        for i in range(MAX_GRAPH):
            d_s = graph_s[ord_a][i]
            d_t = graph_t[ord_b][i]
            if d_s != INF and d_t != INF:
                res.append((i, d_s + d_t))
        if len(res) <= 0:
            print("You will never meet.", end='')
        else:
            res.sort(key=lambda element: element[1])
            for i in range(len(res)):
                if i == 0:
                    print(res[i][1], end=' ')
                if res[i][1] == res[0][1]:
                    print(chr(res[i][0] + CHAR_ORD), end=' ')
        print('')


if __name__ == '__main__':
    main()
