t = int(input())

for _ in range(t):
    n = int(input())
    counter = 0
    rem_a = n
    rem_b = n
    team_a = 0
    team_b = 0
    s = str(input())
    for result in range(len(s)):
        
        counter += 1
    
        if result % 2 == 0:
            rem_a -= 1
            if rem_a == 0 and rem_b == 0:
                print(counter)
                break
        
            elif s[result] == '1':
                team_a += 1
                if team_a > team_b + rem_b:
                    print(counter)
                    break
            else:
                if team_b > team_a + rem_a:
                    print(counter)
                    break
        
        elif result % 2 == 1:
            rem_b -= 1
            if rem_a == 0 and rem_b == 0:
                print(counter)
                break
            elif s[result] == '1':
                team_b += 1
                if team_b > team_a + rem_a:
                    print(counter)
                    break
            else:
                if team_a > team_b + rem_b:
                    print(counter)
                    break
