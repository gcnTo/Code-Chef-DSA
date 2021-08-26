t = int(input())

for _ in range(t):
    k, d0, d1 = map(int,input().split())
    s = str(d0) + str(d1) + str((d0+d1) % 10)
    if s[-1] == "1":
        s += 100 * "2486"
    elif s[-1] == "2":
        s += 100 * "4862"
    elif s[-1] == "3":
        s += 100 * "6248"
    elif s[-1] == "4":
        s += 100 * "8624"
    elif s[-1] == "5":
        s += 100 * "0"
    elif s[-1] == "6":
        s += 100 * "2486"
    elif s[-1] == "7":
        s += 100 * "4862"
    elif s[-1] == "8":
        s += 100 * "6248"
    elif s[-1] == "9":
        s += 100 * "8624"
    elif s[-1] == "0":
        s += 100 * "0"
        
    s = s[:k]

    if len(s) > 100:
        pattern = s[3:7]
        n = int(s[:3])
        
        if pattern == "2486":
            if (k-3) % 4 == 0:
                rem = (((k-3) // 4) * 2) % 3
            elif (k-3) % 4 == 1:
                rem = (((k-3) // 4) * 2 + 2) % 3
            elif (k-3) % 4 == 2:
                rem = (((k-3) // 4) * 2 + 2 + 4) % 3
            elif (k-3) % 4 == 3:
                rem = (((k-3) // 4) * 2 + 2 + 4 + 8) % 3
        
        elif pattern == "4862":
            if (k-3) % 4 == 0:
                rem = (((k-3) // 4) * 2) % 3
            elif (k-3) % 4 == 1:
                rem = (((k-3) // 4) * 2 + 4) % 3
            elif (k-3) % 4 == 2:
                rem = (((k-3) // 4) * 2 + 4 + 8) % 3
            elif (k-3) % 4 == 3:
                rem = (((k-3) // 4) * 2 + 4 + 8 + 6) % 3
        
        elif pattern == "8624":
            if (k-3) % 4 == 0:
                rem = (((k-3) // 4) * 2) % 3
            elif (k-3) % 4 == 1:
                rem = (((k-3) // 4) * 2 + 8) % 3
            elif (k-3) % 4 == 2:
                rem = (((k-3) // 4) * 2 + 8 + 6) % 3
            elif (k-3) % 4 == 3:
                rem = (((k-3) // 4) * 2 + 8 + 6 + 2) % 3
        
        elif pattern == "6248":
            if (k-3) % 4 == 0:
                rem = (((k-3) // 4) * 2) % 3
            elif (k-3) % 4 == 1:
                rem = (((k-3) // 4) * 2 + 6) % 3
            elif (k-3) % 4 == 2:
                rem = (((k-3) // 4) * 2 + 6 + 2) % 3
            elif (k-3) % 4 == 3:
                rem = (((k-3) // 4) * 2 + 6 + 2 + 4) % 3
        elif pattern == "0000":
            rem = 0
            
        if (n + rem) % 3 == 0:
            print("YES")
        else:
            print("NO")
    else:
        if int(s) % 3 == 0:
            print("YES")
        else:
            print("NO")
