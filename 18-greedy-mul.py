def pow2(el):
    c = 0
    while el > 1:
        if el % 2 == 0:
            el //=2
            c += 1
        else:
            break
    return c

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        s = 0
        i = 1
        for el in a: 
            s += pow2(el)
            a[i-1] = pow2(i)
            i += 1
        if s >= n:
            print(0)
        else:
            a.sort(reverse=True)
            cnt = 0
            flag = False
            # print(s, n, ind)
            for pow in a:
                if pow > 0:
                    s += pow
                    cnt += 1
                    if s >= n:
                        flag = True
                        print(cnt)
                        break
                else:
                    break
            if not flag: print(-1)
    