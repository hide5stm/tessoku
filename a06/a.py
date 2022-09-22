def main():
    n, q = [int(v.strip()) for v in input().split()]
    vs = [int(v.strip()) for v in input().split()]
    lrs = []
    for _ in range(q):
        lrs.append([int(v.strip()) for v in input().split()])


    m = len(vs)
    ws = [0] * (m + 1)
    for i in range(m):
        ws[i+1] = ws[i] + vs[i]

    for l, r in lrs:
        print(ws[r] - ws[l - 1])
        
    
if __name__ == '__main__':
    main()
