from collections import defaultdict
 
def cnt(a):
    c = 0
    for el in a: 
        if el == 1: c += 1
    return c
 
def bit_or(a1, a2):
    res = []
    for i in range(len(a1)):
        bit = a1[i] | a2[i]
        res.append(bit)
    return res
 
if __name__ == "__main__":
    t = int(input())
    while t>0:
        n = int(input())
        days = [[] for _ in range(5)]
        g = int(n/2)
        d = defaultdict(list)
        for i in range(n):
            pref = list(map(int, input().split()))
            for j in range(5):
                days[j].append(pref[j])
        sched = []
        for day in days:
            if cnt(day) >= g: 
                sched.append(day)
        flag = False
        for i in range(len(sched)):
            for j in range(i+1, len(sched)):
                a1, a2 = sched[i], sched[j]
                a3 = bit_or(a1, a2)
                if cnt(a3) == n:
                    flag = True
                    break
            if flag:
                break
        if flag: print('YES')
        else: print('NO')
        t -= 1