import queue


class Case:
    def __init__(self, id, time):
        self.id = id
        self.time = time


if __name__ == '__main__':

    c = int(input())

    while c > 0:
        n, t, m = map(int, input().split())
        ql = queue.Queue()
        qr = queue.Queue()
        tempCase = m
        lst = [0] * m
        for i in range(m):
            timeI, side = input().split()
            if side == 'left':
                ql.put(Case(i, int(timeI)))
            else:
                qr.put(Case(i, int(timeI)))
        time = 0
        phaSide = 0

        while not ql.empty() or not qr.empty():
            load = 0
            if qr.empty():
                time = max(time, ql.queue[0].time)
            elif ql.empty():
                time = max(time, qr.queue[0].time)
            else:
                time = max(time, min(ql.queue[0].time, qr.queue[0].time))
            if not phaSide:
                while not ql.empty() and ql.queue[0].time <= time and load < n:
                    load += 1
                    temp = ql.get().id
                    lst[temp] = time + t
                time += t
                phaSide = 1
            else:
                while not qr.empty() and qr.queue[0].time <= time and load < n:
                    load += 1
                    lst[qr.get().id] = time + t
                time += t
                phaSide = 0
        while not ql.empty():
            ql.get()
        while not qr.empty():
            qr.get()
        for i in lst:
            print(i)
        if c > 1:
            print("")
        c -= 1

# Ferry Loading III

# INPUT
# 2
# 2 10 10
# 0 left
# 10 left
# 20 left
# 30 left
# 40 left
# 50 left
# 60 left
# 70 left
# 80 left
# 90 left
# 2 10 3
# 10 right
# 25 left
# 40 left

#OUTPUT
# 10
# 30
# 30
# 50
# 50
# 70
# 70
# 90
# 90
# 110
#
# 30
# 40
# 60