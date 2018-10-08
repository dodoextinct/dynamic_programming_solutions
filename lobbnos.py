def fact(n,m):
    fac = [0 for i in range(n+1)]
    fac[0] = 1
    for i in range(1, n+1):
        fac[i] = i*fac[i-1]
    return fac[n], fac[n-m], fac[m]

for i in range(int(input())):
    n,m = map(int, input().split())
    a,b,c = fact(2*n, m+n)

    print(((2* m+1) * (a//(b*c))) // (m+n+1))
    
