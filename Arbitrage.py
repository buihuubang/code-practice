def floyd_warshall1(graph, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] < graph[i][k] * graph[k][j]:
                    graph[i][j] = graph[i][k] * graph[k][j]
    for i in range(n):
        if graph[i][i] > 1.0:
            return True
    return False


def main():
    count = 1
    while True:
        n = input()
        if len(n.strip()) > 0:
            n = int(n)
            if n == 0:
                break
            dictName = {}
            for i in range(n):
                name = input()
                dictName[name] = i
            m = int(input())
            graph = [[0.0 for i in range(n)] for j in range(n)]
            for i in range(m):
                s, w, e = input().split()
                graph[dictName[s]][dictName[e]] = float(w)
            if floyd_warshall1(graph, n):
                print(f'Case {count}: Yes')
            else:
                print(f'Case {count}: No')
            count += 1


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
3
USDollar
BritishPound
FrenchFranc
3
USDollar 0.5 BritishPound
BritishPound 10.0 FrenchFranc
FrenchFranc 0.21 USDollar

3
USDollar
BritishPound
FrenchFranc
6
USDollar 0.5 BritishPound
USDollar 4.9 FrenchFranc
BritishPound 10.0 FrenchFranc
BritishPound 1.99 USDollar
FrenchFranc 0.09 BritishPound
FrenchFranc 0.19 USDollar

0


OUTPUT:
Case 1: Yes
Case 2: No
'''