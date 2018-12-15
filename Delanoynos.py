def dp(n,m):

    l = [[0 for i in range(n+1)] for i in range(m+1)]

    for i in range(m):
        l[0][i] = 1
    for j in range(m+1):
        l[j][0] = 1

    for i in range(1, m+1):
        for j in range(1,n+1):
            l[i][j] = l[i-1][j] + l[i-1][j-1]+l[i][j-1]
    return l[m][n]
    

for i in range(int(input())):
    n,m = map(int, input().split())
    
    print(dp(n,m))



    
