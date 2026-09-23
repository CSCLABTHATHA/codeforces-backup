n = int(input())
ret = []
for _ in range(n):
    s = input()
    t = input()

    
    while True:
        if t[0] in s:
                cursor = s.index(t[0])
                curcache = cursor
        else:
            ret.append("No")
            continue
        
        for ind in range(1,len(t)):
            char = t[ind]
            if cursor != len(t)-2 and char == s[cursor + 1]:
                cursor += 1
            elif cursor != 0 and char == s[cursor -1]:6
                cursor -= 1
            else:
                if t[0] in s[curcache]:
                    cursor = curcache + s[curcache + 1:].index(t[0])
                    curcache = cursor
                else:
                    ret.append("No")
                    break
        else:
            ret.append("Yes")
            break


print(*ret,sep='\n')