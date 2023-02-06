import sys

n = int(input())
l, h = 1, n
while l<=h:
    m = (l+h)//2

    # query the set
    if m!=1:
        print(f'? {str(m-1)}'); sys.stdout.flush()
        prev = int(input())
    else:
        prev = float('inf')
    print(f'? {str(m)}'); sys.stdout.flush()
    curr = int(input())
    if m != n:
        print(f'? {str(m+1)}'); sys.stdout.flush()
        nxt = int(input())
    else:
        nxt = float('inf')

    if prev > curr and curr < nxt:
        print(f'! {str(m)}')
        break
    elif curr > prev:
        h = m-1
    else:
        l = m+1