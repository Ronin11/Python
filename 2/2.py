def increment(x):
	return x+1

def add(x, y):
	return x+y

def pow(num, power):
	var = num
	for i in range(1, power):
		num *= var
	return num

def callFunc(f, x):
	return f(x)

def callFunc(f, x, y):
	return f(x, y)

def fx(x):
	return pow(x,3) - x*2 - 5

def dfx(x):
	return pow(x,2)*3 - 2

def fx2(x):
	return pow(x,6) - 2

def dfx2(x):
	return pow(x,5)*6

def nrMethod(x, fx, dfx):
	return x - float(fx(x))/float(dfx(x))

def newtonRaphson(x, fx, dfx):
	value = nrMethod(x,fx,dfx)
	while(value != 0):
		temp = nrMethod(value,fx,dfx)
		if(value == temp):
			return value
		else:
			print value
			value = temp	
