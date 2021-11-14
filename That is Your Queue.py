import queue


if __name__ == '__main__':
    lst = []
    count = 1
    while True:
        n, c = map(int, input().split())
        if n == 0 and c == 0:
            break
        else:
            lst = []
            q = queue.Queue()
            print("Case " + str(count) + ":")
            n = min(2*c, n)
            for i in range(1, n + 1):
                q.put(i)
            while c > 0:
                lst = input().split()
                if len(lst) < 2:
                    # print(list(q.queue))
                    print(q.queue[0])
                    q.put(q.get())
                else:
                    temp = 0
                    q_help = queue.Queue()
                    num_e = int(lst[1])
                    if num_e > n:
                        q.put(num_e)
                    while not q.empty():
                        if q.queue[0] != num_e:
                            q_help.put(q.get())
                        else:
                            q.put(q.get())
                            break
                    while not q_help.empty():
                        q.put(q_help.get())
                    while q.queue[0] != num_e:
                        q.put(q.get())
                c -= 1
            count += 1

# TEST CASE:

# INPUT:
# 3 6
# N
# N
# E 1
# N
# N
# N
# 10 2
# N
# N
# 0 0

# OUT PUT:
# Case 1:
# 1
# 2
# 1
# 3
# 2
# Case 2:
# 1
# 2
