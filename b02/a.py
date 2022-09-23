def main():
    a, b = [int(v.strip()) for v in input().split()]

    for k in range(a, b + 1):
        if 100 % k == 0:
            print("Yes")
            return

    print("No")

if __name__ == '__main__':
    main()
