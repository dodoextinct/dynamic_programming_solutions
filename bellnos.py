for i in range(int(input())):
    n = int(input())

    l = [[0 for i in range(n+10)] for j in range(n+1)]
    l[0][0] = 1
    
    for i in range(1, n+1):
        l[i][0] = l[i-1][i-1]

        for j in range(1, i+1):
            l[i][j] = l[i-1][j-1] + l[i][j-1]

    print(l[n][0])
