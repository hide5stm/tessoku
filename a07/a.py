def main():
    d = int(input())
    n = int(input())
    lrs = []
    for _ in range(n):
        lrs.append([int(v.strip()) for v in input().split()])

    # 日付の配列
    ds = [0] * (d + 1) # 最終日+1の分確保
    for l, r in lrs:
        ds[l-1] += 1 # 出席開始日で加算
        ds[r] -= 1 # 出席終了の次の日に減算

    # 累積和計算
    ws = [0] * (d + 1)
    for i in range(len(ws)-1):
        ws[i+1] = ws[i] + ds[i]

    for w in ws[1:]: # 最初は計算上の余白なので不要
        print(w)

if __name__ == '__main__':
    main()
