from math import floor, sqrt


def simpleSieve(limit, primes):
	mark = [False]*(limit+1)

	for i in range(2, limit+1):
		if not mark[i]:
			# If not marked yet, then its a prime
			primes.append(i)
			for j in range(i, limit+1, i):
				mark[j] = True


# Finds all prime numbers in given range using
# segmented sieve
def primesInRange(low, high):

	# Comput all primes smaller or equal to
	# square root of high using simple sieve
	limit = floor(sqrt(high)) + 1
	primes = list()
	simpleSieve(limit, primes)
	# Count of elements in given range 
	n = high - low + 1
	
	# Declaring boolean only for [low, high] 
	mark = [False]*(n+1) 

	# Use the found primes by simpleSieve() to find 
	# primes in given range 
	for i in range(len(primes)): 
		# Find the minimum number in [low..high] that is 
		# a multiple of prime[i] (divisible by prime[i]) 
		loLim = floor(low/primes[i]) * primes[i] 
		if loLim <= low: 
			loLim += primes[i] 
		for j in range(loLim, high+1, primes[i]): 
			mark[j-low] = True

	# Numbers which are not marked in range, are prime 
	for i in range(low, high+1): 
		if not mark[i-low]: 
			print(i, end = " ") 



# Driver program to test above function 
low = 7
high = 20
primesInRange(low, high) 
