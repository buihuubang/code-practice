def check(a, n, jump):
    for i in range(n):
        if a[i] > jump:
            return False
        if a[i] == jump:
            jump -= 1
    return True


def bis(a, l, r, n):
    pos = 0
    while l <= r:
        mid = l + (r - l)//2
        if check(a, n, mid):
            pos = mid
            r = mid - 1
        else:
            l = mid + 1
    return pos


def main():
    tc = int(input())
    for i in range(1, tc + 1):
        n = int(input())
        a = list(map(int, input().split()))
        sub = [a[0] if j == 0 else a[j] - a[j - 1] for j in range(n)]
        print(f"Case {i}: {bis(sub, 0, a[n-1], n)}")


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
2
5
1 6 7 11 13
4
3 9 10 14

OUTPUT:
Case 1: 5
Case 2: 6
'''