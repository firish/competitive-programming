if __name__ == "__main__":
    l, h = 1, 10**18
    m = (l+h)//2
    print(m) # guess
    f = input()
    while l <= h or f=='CORRECT':
        if f == 'CORRECT':
            break
        elif f == 'HIGHER':
            l = m + 1
        else:
            h = m - 1
        m = (l+h)//2
        print(m)
        f = input()
