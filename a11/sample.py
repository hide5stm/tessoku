import random

def main():
    m = 99
    ans = 10
    vs = list(range(1, m, 2))
    vs.append(ans)
    vs.sort()
    print(len(vs), ans)
    print(" ".join(str(v) for v in vs))
    #print(vs)
    
    
if __name__ == '__main__':
    main()



