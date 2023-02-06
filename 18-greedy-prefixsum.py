for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if k == 1: 
        print("YES")
        continue
    presum = []
    presum_rev = []
    for i in range(1, k):
        presum.append(arr[i] - arr[i - 1])
        presum_rev.append(arr[i] - arr[i - 1])
    presum_rev.sort()
    if presum_rev != presum:
        print("No")
        continue
    if (n-(k-1)) * presum[0] < arr[0]: 
        print("No")
    else:
        print("Yes")