if __name__ == "__main__":
    t = int(input())
    i = 1
    while t>0:
        l, w, h = map(int, input().split())
        if l <= 20 and w <= 20 and h <= 20: print(f'Case {i}: good')
        else: print(f'Case {i}: bad')
        i += 1
        t -= 1
