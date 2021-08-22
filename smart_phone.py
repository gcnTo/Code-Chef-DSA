n = int(input())
l = []

# Populating the list of customer budgets.
for i in range(n):
    l.append(int(input()))

l = sorted(l) #Sorts the list l for efficiency.
top = 0

# Since l is sorted, we know that each l[i] < l[i+1]
# And since we only have a deal if l[i] <= customer budget,
# we know that each l[i] needs to be multiplied by (n-i) elements, 
# because all the budgets ((n-i) budgets) following l[i] are more than l[i]
for i in range(n):
    if l[i] * (n-i) > top: 
        top = l[i] * (n-i)

print(top)
