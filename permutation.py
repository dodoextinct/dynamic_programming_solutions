for i in range(int(input())):
    n,r = map(int, input().split())
    fact = [0 for i in range(n+1)]

    fact[0] = 1

    for i in range(1,n+1):

        fact[i] = i * fact[i-1]

        return fact[n] / fact[n-r]


