MAX_N = 100001
def prime_factors(n):
    spf = [-1 for i in range(MAX_N)]
    spf[1] = 1
    for i in range(2,MAX_N):
        if spf[i] == -1:
            spf[i] = i
            for j in range(i,MAX_N,i):
                if spf[j] == -1:
                    spf[j] = i
    while n!=1:
        print(spf[n])
        n = n//spf[n]
prime_factors(45)

        