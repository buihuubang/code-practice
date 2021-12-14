def main():
    n = int(input())
    d = dict()
    for i in range(n):
        s = input()
        if d.get(s) == None:
            d[s] = 1
        else:
            d[s] = d.get(s) + 1
    od = {k: v for k, v in sorted(d.items(), key=lambda v: -v[1])}
    od = list(od)
    print(od[0])


if __name__ == '__main__':
    main()

'''
TEST CASE:

INTPUT:
7
Emperor Penguin
Macaroni Penguin
Little Penguin
Emperor Penguin
Macaroni Penguin
Macaroni Penguin
Little Penguin

OUTPUT:
Macaroni Penguin
'''