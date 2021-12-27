## Write a procedure that takes an argument n and returns the largest power of 2 that is smaller than n
## This is a variant that gives the exponent for that power. Note this only supplies positive integer exponents.
def pow2sm(n):
	e = 1  # exponent assigned start value.  
	while 2**e < n:
		e = e+1
	return e-1    # e-1 since the while loop terminates when 2**e > n thus e would be e+1 at the time.
