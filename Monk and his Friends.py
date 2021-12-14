def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        lst = list(map(int, input().split()))
        d = dict()
        for i in range(n):
            d[lst[i]] = 1
        for i in range(m):
            if d.get(lst[i + n]) != None:
                print('YES')
            else:
                print('NO')
                d[lst[i + n]] = 1


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
1
2 3
3 2 9 11 2

OUTPUT:
NO
NO
YES
'''