t = int(input())

for i in range(t):
    g = int(input())
    
    for j in range(g):
        i,n,q = map(int,input().split())
        
        # If n is even, Heads = Tails no matter what according to the problem statement.
        if n % 2 == 0:
            heads = n // 2
            tails = n - heads
        else:
        # If n is odd, "Number of Heads will be less than Number of Tails, if all coins were Heads initially" and vice versa
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
