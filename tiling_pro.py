#code

for i in range(int(input())):
    n = int(input())
    
    l = [1 for i in range(n+1)]
    
    for i in range(2, n+1):
        l[i] = l[i-1] + l[i-2]
        
    print(l[n])
