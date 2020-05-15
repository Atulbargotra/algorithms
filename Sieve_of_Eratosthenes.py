def print_sieve(n):
    sieve = [True for i in range(n+1)]
    i = 2
    while i*i<=n:
        if sieve[i] == True:
            for j in range(i*i,n+1,i):
                sieve[j] = False
        i+=1
    for i in range(2,n+1):
        if sieve[i]:
            print(i,end=" ")

if __name__ == '__main__':
    n = int(input())
    print_sieve(n)
    #Time complexity : O(n*log(log(n)))         