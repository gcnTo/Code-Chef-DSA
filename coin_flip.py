t = int(input())

for i in range(t):
    g = int(input())
    
    for j in range(g):
        i,n,q = map(int,input().split())
        if n % 2 == 0:
            heads = n // 2
            tails = n - heads
        else:
            if i == 1:
                heads = n // 2
                tails = n - heads
            elif i == 2:
                tails = n // 2
                heads = n - tails
        if q == 1:
            print(heads)
        elif q == 2:
            print(tails)
