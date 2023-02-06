def get_bin(x):
    arr = [0]*31 # constraint in question
    b = 30
    ones = []
    while x > 0:
        v = x%2
        if v == 1: 
            ones.append(b)
        arr[b] = v
        x = int(x/2)
        b -= 1
    return (arr, ones)

if __name__ == "__main__":
    t = int(input())
    while t>0:
        x = int(input())
        y = [0]*31
        x2, ones = get_bin(x)
        # print(x2, ones)
        if len(ones) == 1:
            y[ones[0]] = 1
            if ones[0] == 30: y[29] = 1
            else: y[30] = 1
        else: 
            y[ones[0]] = 1

        # convert back to decimal and print
        dec = [0]*31
        b = 30
        for i in range(31):
            dec[i] = y[b]
            b -= 1
        print(int(''.join(map(str,dec))[::-1], 2))
        t -= 1

