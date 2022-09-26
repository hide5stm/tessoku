def main():
    n, x = [int(v.strip()) for v in input().split()]
    vs = [int(v.strip()) for v in input().split()]

    i = len(vs) // 2
    s, e = 0, len(vs)
    while True:
        v = vs[i]
        if v == x:
            print(i + 1)
            break
        elif v < x:
            s = i
            i = (e - i) // 2 + i
        else:
            e = i
            i = e // 2

if __name__ == '__main__':
    main()
