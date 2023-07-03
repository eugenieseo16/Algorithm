while True :
    try :
        s, t = input().split()

        flag = 0
        num = 0
    
        for i in range(len(t)):
            if t[i] == s[num]:
                num +=1
                if num == len(s):
                    flag = 1
                    break
    
        if flag == 1:
            print('Yes')
        else:
            print('No')
    except :
        break