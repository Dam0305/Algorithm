t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    if n%h == 0:
        print("%d%d%d"%(h, 0, n//h) if n//h < 10 else "%d%d"%(h, n//h))
    else:
        print("%d%d%d" % (n % h, 0, n // h + 1) if n // ah + 1 < 10 else "%d%d" % (n % h, n // h + 1))
