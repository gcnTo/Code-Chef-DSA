n = int(input())
l = []

for i in range(n):
    l.append(int(input()))

l = sorted(l)
top = 0
candidate = 0

for k in range(len(l)):
    minus = l[k]
    candidate = 0
    for j in range(len(l)):
        if l[j] >= minus:
            candidate += minus
            if candidate > top:
                top = candidate

print(top)
