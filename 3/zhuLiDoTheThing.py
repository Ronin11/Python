import random

def modPow(num, pow, mod):
	i = 1;
	for i in range(1, pow):
		i *= num
		i %= mod
	return i % mod
def isPrime(num, iterations):
	if(num == 1 or num == 0):#0 and 1 are defined to be not prime
		return str(num)+" is not prime"
	elif(num == 2):#2 is prime
		return str(num)+" is prime"
	elif(num % 2 == 0):#Anything divisible by 2 is obviously not prime
		return str(num)+" is not prime"
	random.seed()
	for i in range(1, iterations):
		rand = random.randrange(1,num-1,1)
		num2 = rand % (num - 1) +1
		if(modPow(num2, num-1,num) == 1):
			return str(num)+" is probably prime"
		else:
			return str(num)+" is not prime"
	
