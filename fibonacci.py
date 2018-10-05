
for i in range(int(input())):
    n = int(input())
    
    d = [0] * (n+1)
    
    d[0]= 0
    d[1] = 1
    d[1] = 1
        
    for i in range(2,n+1):
        d[i] = (d[i-1]+d[i-2]) % (10**9 + 7)
            
    print(d[n])
