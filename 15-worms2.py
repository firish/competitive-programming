n = int(input())
pile = []
worms =  list(map(int, input().split()))
bucket = 1
for worm in worms:
    temp = [bucket]*worm
    pile += temp
    bucket += 1
w = int(input())
juicy = list(map(int, input().split()))
for j in juicy:
    print(pile[j-1])