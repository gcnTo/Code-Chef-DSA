n = int(input())
budget = []

# Populating the list of customer budgets.
for i in range(n):
    budget.append(int(input()))

budget = sorted(budget) #Sorts the list of budgets for efficiency.
top = 0

# Since the list budget is sorted, we know that each budget[i] < budget[i+1]
# And since we only have a deal if budget[i] <= customer budget,
# and all the budgets ((n-i) budgets) following budget[i] are more than budget[i]
# we know that each budget[i] needs to be multiplied by (n-i) elements, 
for i in range(n):
    if budget[i] * (n-i) > top: 
        top = budget[i] * (n-i)

print(top)
