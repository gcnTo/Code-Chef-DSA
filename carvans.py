t = int(input())

for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    counter = 0
    for i in range(n):
        if i+1 < n:
            if l[i] < l[i+1]: #Compares speeds of two back to back cars.
                counter += 1 #Counts the number of cars that are not moving on their max speed.
                l[i+1] = l[i]
    print(n - counter) #Prints the number of cars that are moving on their max speed.
