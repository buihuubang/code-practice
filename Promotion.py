import heapq

class PQEntry:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value


if __name__ == '__main__':
    n = int(input())
    minLst = []
    maxLst = []
    sumCost = 0
    lenLst = 0
    for i in range(n):
        b = list(map(int, input().split()))
        for j in range(1, len(b)):
            heapq.heappush(minLst, b[j])
            heapq.heappush(maxLst, PQEntry(b[j]))
            lenLst += 1
        if lenLst >= 2:
            maxCost = heapq.heappop(maxLst)
            minCost = heapq.heappop(minLst)
            sumCost += (maxCost.value - minCost)
            maxLst.pop()
            minLst.pop()
            lenLst -= 2
    print(sumCost)

'''
TEST CASE:

INPUT:
5
3 1 2 3
2 1 1
4 10 5 5 1
0
1 2

OUTPUT:
19

'''