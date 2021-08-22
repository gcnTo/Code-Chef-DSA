t = int(input())
d1 = {}
d2 = {}

for i in range(t):
    s = str(input())
    d1 = {}
    d2 = {}
    truth = 0
    lens = len(s) // 2
    
    if len(s) % 2 == 0:
        s1 = s[:lens] #First half of the string.
        s2 = s[lens:] #Second half of the string.
    elif len(s) % 2 == 1:
        s1 = s[:lens] #First half of the string.
        s2 = s[lens+1:] #Second half of the string.
    
    #Populates dict 1 to record how many times a letter is in the string s1.
    for j in range(len(s1)): 
        if s1[j] in d1:
            d1[s1[j]] += 1 
        else:
            d1[s1[j]] = 1
    
    #Populates dict 2 to record how many times a letter is in the string s2.
    for k in range(len(s2)): 
        if s2[k] in d2:
            d2[s2[k]] += 1
        else:
            d2[s2[k]] = 1
            
    #Compares dict 1 and dict 2 to see if the all contain the same letters the same number of times.
    for item in d1: 
        if item in d2:
            if d1[item] == d2[item]:
                truth += 1
    
    if truth == len(d1):
        print("YES")
    elif truth != len(d1):
        print("NO")
