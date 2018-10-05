#code
for i in range(int(input())):
    n,r = map(int, input().split())
    
    dp = [0 for i in range(r+1)]
    
    dp[0] = 1
    
    for i in range(1, n+1):
        
        for j in range(min(i,r), 0 , -1):
            
            dp[j] = (dp[j] + dp[j-1]) % (10**9 + 7)
            
    print(dp[r])
    
