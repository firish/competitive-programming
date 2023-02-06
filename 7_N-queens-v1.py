if __name__ == "__main__":
    k,rows,cols = map(int,input().split())
    c, kc = 0, 0
    colset, posd, negd = set(), set(), set()
    def backtrack(r, kc):
        global c
        if k == kc:
            c += 1
            return 
        for col in range(cols):
            for row in range(r, rows):
                if col in colset or (row+col) in posd or (row-col) in negd:
                    continue
                kc += 1
                colset.add(col)
                posd.add(row+col)
                negd.add(row-col)
                backtrack(row+1, kc)
                negd.remove(row-col)
                posd.remove(row+col)
                colset.remove(col)
                kc -= 1
    backtrack(0, kc)
    print(c)




        
