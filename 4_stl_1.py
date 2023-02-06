if __name__ == "__main__":
    n, m = map(int, input().split())
    h = {}
    for i in range(n):
        name, ip = input().split()
        h[ip] = name
    for i in range(m):
        cmd, ip = input().split()
        print(cmd + " " + ip + " #" + h[ip[:-1]])
