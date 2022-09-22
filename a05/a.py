def main():
    n, k = [int(v.strip()) for v in input().split()]

    c = 0
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            z = k - x - y
            if 1 <= z and z <= n:
                c += 1
                #print(x, y, k - x - y)

    print(c)


if __name__ == '__main__':
    main()
