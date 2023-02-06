t = int(input())
for _ in range(t):
    n, b, x, y = map(int, input().split())
    curr, s = 0, 0
    for i in range(1, n+1):
        if curr+x <= b: curr += x
        else: curr -= y    
        s += curr
    print(s)
