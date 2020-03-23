'''def sqr(m):
	k = m * m 
	return k
print(sqr(3))

def f1(n):
    try: 
	    int(n)
    except ValueError:
	    print('this not number')
    else:
        n = str(n)
        print(' '.join(n))
       
f1(231)

def sqr(m):
    try:
        int(m)
    except ValueError:
        print('This not number')
    else:
        k = m*m
    return k 

print(sqr(4))'''

def fib_nest(l):
	if l > 0:
		if l == int(l):
			f, s = 1, 2
			while f <= l:
				if f == l:
					return s
				f, s = s, f + s 
	raise ValueError('{} is wrong'.format(l))



k =1
if k == int(k):
	print("312312312")
def num_split(n):
	try:
		int(n)
	except ValueError:
		print('This not number')
	else:
		if n >= 0:
			summa = 0
			dobb = 1
			h = len(str(n))
			n = list(str(n))
			for i in range(len(n)):
				k = int(n[i])
				summa = summa + k
				dobb = dobb * k
			test = (h,summa,dobb)
			return test 

print(num_split(23892344))


def num_split123123(n):
	try:
		int(n)
		test = []
		n = list(str(n))
		if n > 0:
			for m in n :
				k = int(m)
				test.append(k)
			return test
	except ValueError:
		print('This not number')
print(num_split123123(123123234567890))


def fibb(l):
	f, s = 1, 2
	while l >= f:
		if f == l:
			return s
		f, s = s, f + s 
	raise ValueError('{} is wrong'.format(l))

print(fibb(2))


def simple(n):
	try:
		if n < 0:
		    return False
		if n < 2:
		    return False
		if n == int(n):
		    for i in range (2,n):
			    k = n % i
			    if k == 0:
				    return False
		    return True
	except ValueError:
		return False
print(simple(123123))

def simple2(n):
	result = []
	for numbers in n:
		if simple(numbers)  == True:
			result.append(numbers)			
	return(result)
print(simple2(range(10)))



def palidromes(n):
	result = []
	end = []
	for numbers in n:
		l = list(str(numbers))
		r = list(reversed(l))
		if l == r:
			result.append(l)
	for numbers in result:
		k = ''.join(numbers)
		end.append(k)
	end = sorted(end)
	return end

print(palidromes([212,666,343,54667,444,555]))

def matrix(n):
	copy = list(zip(*n))
	return copy
	


print(matrix([[2,1,3],[4,6,8]]))



def posl(n):
	copy = list(str(n))
	k = []
	result = []
	for numbers in copy:
		k.append(numbers) 
		if  len(k) == 13:
			a = 1
			for m in k:
				a = a*int(m)
			result.append(a)
			k = []
	result = sorted(result)
	print(result)
posl(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)


'''j= 313123
try: 
	int(j)
except ValueError:
	print('this not number')
else:
	j = str(j)
	for number in j:
		print(' '.join(j))
	print(j)'''
int('12323.34324')