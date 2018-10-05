for i in range(int(input())):
    n = int(input())
    
    l = [None] * (n+1)
    
    l[0] = 1
    l[1] = 1
    def fact(n):
        fac = 1
        while(n >=1):
            fac *= n
            n = n-1
        return fac
        
    print(fact(2*n)//(fact(n+1)*fact(n)))
