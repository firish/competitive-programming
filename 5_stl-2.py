if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        print(a[-1]-a[0]+a[-2]-a[1])
        t -= 1