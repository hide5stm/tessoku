def main():
    n, x = [int(v.strip()) for v in input().split()]
    vs = [int(v.strip()) for v in input().split()]

    if x in vs:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
