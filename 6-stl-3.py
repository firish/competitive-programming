from collections import defaultdict
from collections import deque

if __name__ == "__main__":
    n, c = map(int, input().split())
    u = 0
    pos = 1
    h = defaultdict(list)
    q = deque()
    tick = [0]*(c+1)
    for i in range(c):
        t1, t2 = map(int,input().split())
        if t1 == 1:
            q.append((t2, pos))
            h[t2].append(pos)
            pos += 1
            u += 1
        elif t1 == 2:
            for j in h[t2]:
                if tick[j] == 0:
                    u -= 1
                    tick[j] = 1
            h[t2] = []
        else:
            while q and t2 >= q[0][1]:
                pt = q.popleft()
                if tick[pt[1]] == 0:
                    u -= 1
                    tick[pt[1]] = 1
        print(u)