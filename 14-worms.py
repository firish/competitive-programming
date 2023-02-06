n = int(input())
a = []
pile = 0
presum = 0
worms =  list(map(int, input().split()))
for worm in worms:
    a.append(presum + worm)
    presum += worm
    pile += 1
w = int(input())
juicy = list(map(int, input().split()))
for j in juicy:
    l, h = 0, n
    flag = False
    while l<=h:
        m = (l+h)//2
        if j == a[m]:
            print(m+1)
            flag = True
            break
        elif j < a[m]:
            h = m-1
        else:
            l = m+1
    if not flag: print(l+1)
