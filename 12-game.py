# def check(mh, ma, dh, da):
#     flag = False
#     # base case for handling big healths and low attacks
#     print(dh/ma, mh/da)
#     while mh > 0:
#         dh -= ma
#         if dh <= 0:
#             flag = True
#             break
#         mh -= da
#     if flag: return True
#     else: return False
import math
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        mh, ma = map(int,input().split())
        dh, da = map(int,input().split())
        k,w,a = map(int,input().split())
        for i in range(k+1):
            ma2 = ma + (i*w)
            mh2 = mh + ((k-i)*a)
            # res = check(mh2, ma2, dh, da)
            res = False
            if math.ceil(mh2/da) >= math.ceil(dh/ma2):
            # if res == True:
                print('YES')
                res = True
                break
        if not res: print('NO')


