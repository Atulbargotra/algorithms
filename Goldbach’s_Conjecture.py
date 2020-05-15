def sieve_of_sundaram(n):
    primes = list()
    nNew = (n-2)//2
    sieve = [0]*(nNew+1)
    for i in range(1,nNew+1):
        j = i
        while((i+j+2*i*j) <= nNew):
            sieve[i+j+2*i*j] = 1
            j+=1
    if n>2:
        primes.append(2)
    for i in range(1,nNew+1):
        if sieve[i] == 0:
            #print((2*i+1),end=" ")
            primes.append(2*i+1)
    return primes
def Goldbatch_Conjective(n):
    primes = sieve_of_sundaram(n)
    if (n <= 2 or n % 2 != 0): 
        print("invalid")
        return
    i = 0
    while(primes[i] <= n//2):
        diff = n - primes[i]
        if diff in primes:
            print(primes[i], "+", diff, "=", n)
            return
        i+=1
n = int(input())
Goldbatch_Conjective(n)
