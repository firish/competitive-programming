t=int(input())
for _ in range(t):
    n=int(input())
    d={'M':[],'T':[],'W':[],'Th':[],'F':[]}
    for i in range(n):
        m,t,w,th,f=map(int,input().split())
        if m==1:d['M'].append(i+1)
        if t==1:d['T'].append(i+1)
        if w==1:d['W'].append(i+1)
        if th==1:d['Th'].append(i+1)
        if f==1:d['F'].append(i+1)
    print(d)
    if n%2!=0:print("NO")
    else:
        l=[]
        for x in d:
            if len(d[x])>=n//2:
                l.append(x)
        if len(l)==1 or len(l)==0:
            print("NO")
        else:
            print(l)
            f=0
            for i in range(len(l)-1):
                for j in range(i+1,len(l)):
                    u=set(d[l[i]]).union(set(d[l[j]]))
                    print(u)
                    if len(u)==n:
                        f=1
                        print("YES")
                        break
                if f==1:
                    break
            if f==0:
                print("NO")