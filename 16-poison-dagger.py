def check(k, e, damage):
    attack = 0
    for d in damage:
        attack += min(d, k)
    attack += k
    if attack >= e: return True
    return False


t = int(input())
for _ in range(t):
    n, e = map(int, input().split())
    damage = []
    a= list(map(int, input().split()))
    for i in range(len(a)-1):
        damage.append(a[i+1]-a[i])
    if n >= e:
        print('1')
    else:
        l, h = e//n, e
        ans = 0
        while l<=h:
            m = (l+h)//2
            if check(m, e, damage):
                ans = m
                h = m - 1
            else:
                l = m + 1             
        print(ans)