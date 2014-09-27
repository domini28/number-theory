import math

def gcd(a,b):
	while b != 0:
                (a, b) = (b, a%b)
        return a

print gcd(20,30) 


def lcm(a,b):
        lcm = (a*b)/gcd(a,b)
        return lcm

print lcm(2,3)
                
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

print egcd(21,300)

def sieve(n):
   if n<=1:return[]
   X=range(3,n+1,2)
   P=[2]
   sqrt_n= math.sqrt(n)
   while len(X)>0 and X[0] <=sqrt_n:
      p = X[0]
      P.append(p)
      X=[a for a in X if a%p !=0]
   return P+X

print sieve(31)





def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

print is_prime(13)                        
                        

        
