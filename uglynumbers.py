for i in range(int(input())):
    n  =int(input())
    c = 0
    for i in range(211):
        
        if(i%2 != 0 and i %3 != 0 and i %5 != 0 and i%7 !=0):
            c+=1
    x = n //210
    c *= x
    for i in range(x*210 +1, n+1):
        if(i%2 != 0 and i %3 != 0 and i %5 != 0 and i%7 !=0):
            c+=1
        
    print(c)
