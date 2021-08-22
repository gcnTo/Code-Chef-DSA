n = int(input())
l = []

for i in range(n):
    l.append(int(input()))

l = sorted(l)
top = 0

for i in range(n):
    if l[i] * (n-i) > top:
        top = l[i] * (n-i)

print(top)
