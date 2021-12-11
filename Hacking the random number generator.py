def bis(a, l, r, x):
    pos = -1
    while l <= r:
        mid = l + (r - l)//2
        if a[mid] >= x:
            pos = mid
            r = mid - 1
        else:
            l = mid + 1
    return pos


def main():
    n, k = map(int, input().split())
    numLst = list(map(int, input().split()))
    numLst.sort()
    count = 0
    for i in range(n):
        find_x = numLst[i] + k
        pos = bis(numLst, 0, n - 1, find_x)
        if numLst[pos] == find_x:
            count += 1
    print(count)


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
5 2
1 5 3 4 2

OUTPUT:
3
'''