for _ in range(int(input())):
    n, k = map(int, input().split())
    depos = list(map(int,input().split()))
    pos, neg = [], []
    for el in depos:
        if el >= 0: pos.append(el)
        else: neg.append(el)
    pos.sort()
    neg.sort(reverse=True)
    
    dist = 0
    for i in range(len(pos)-1, -1, -k):
        dist += 2*pos[i]
    for i in range(len(neg)-1, -1, -k):
        dist += 2*abs(neg[i])
    
    if len(pos) > 0 and len(neg) > 0: ret_dist = max(pos[-1], abs(neg[-1]))
    elif len(pos) > 0: ret_dist = pos[-1]
    else: ret_dist = abs(neg[-1])
    print(dist - ret_dist)
