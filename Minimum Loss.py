def main():
    n = int(input())
    lst = list(map(int, input().split()))
    d = {lst[i]:i for i in range(n)}
    lst.sort()
    minNum = 1e16
    for i in range(1, n):
        if d[lst[i]] < d[lst[i - 1]]:
            minNum = min(minNum, lst[i] - lst[i-1])
    print(minNum)


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
3
5 10 3

OUTPUT:
5
20 7 8 2 5
'''