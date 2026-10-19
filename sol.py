import math
import sympy

def pollard(n):
	a = 2
	i = 2
	
	while(True):
		#a = (a**i) % n
		a = pow(a,i,n)
		d = math.gcd((a-1), n)
		if (d > 1):
			return d
			break
		i += 1

# Driver code
n = 0xa09d5bbe7b77137e4a923e89057edaac71a600b229ad43bd20e56b5aa2e2ddd4a1171322d4af4fa8f48437a7663917f726b225964df20a37df79210694a081f5f28199e35997f52dfcaa5c7b9971b00b02acf2fc2fead62ed0bbc6fd5c275fb5d72ead7fe5b82b9818717acf77d6108fef8a56c5a2307866f8779d336a8f44d0cb8699f4c2db98564fed93e863f48778f802cc9d32b7185cd76a47fec3b056e804a26b4d1b254f055e73ffc08a547ad4bede1d297876140665ae93f04cacb6f88665797d6e48a9ba3d1500f16067adfb5624199e73ccd806c283a399e25b8cc223575112353b3ed24939f98dc33e0ac5298b690995ffcc5ce66d7e9ef976a801
# temporarily storing n
num = n
	
# list for storing prime factors
ans = []
while(True):
	d = pollard(num)
	ans.append(d)

	# r = int(num/d)
	r = num//d
	
	if(sympy.isprime(r)):
		ans.append(r)
		break
	else:
		num = r

# print the result
print("Prime factors of", n, "are", *ans)
