# def binarySearchIndexAndComparisons(L,k):
#     numComp = 0
#     res = False
    
#     while L !=[]:
#         left = 0
#         right = len(L)-1
#         mid = (left+right)//2
#         if L[mid] == k:
#             res = True
#             numComp +=1
#             break
#         elif k > L[mid]:
#             L = L[mid+1:]
#             numComp +=1
#         elif k < L[mid]:
#             L = L[:mid]
#             numComp +=1
#     return (res, numComp)

################################################

#def string_to_integer(s):
#    if not s:
#        return -1
#    if s[0] == '-':
#        if len(s) == 1:
#            return -1
#        s = s[1:]
#        negative = True
#    else:
#        negative = False
#    result = 0
#    for char in s:
#        if not char.isdigit():
#            return -1
#        digit = ord(char) - ord('0')
#        result = result * 10 + digit
#    if negative:
#        result *= -1
#    return result

# Test cases
#print(string_to_integer("123"))  # Output: 123
#print(string_to_integer("-456"))  # Output: -456
#print(string_to_integer("abc"))  # Output: -1 (Invalid input)
#print(string_to_integer('7675895'))

########################################

# MOD = 10**9 + 7
# def ini(n):
#     return ((n * (n+1))//2) + 1

# def T(n):
#     m = 1
#     for i in range(ini(n), ini(n)+n+1):
#         m = m* i
#     return m
# def F(n):
#     if n == 0:
#         return 0
#     if n==1:
#         return T(0)
#     return T(n-1) + F(n-1)
        
        
# print(F(996))



###########################################

# import math

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(math.sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True

###################

# def Find_Min_Difference(L,P):


###################

# class Triangle:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def Is_valid(self):
#         if (self.a + self.b > self.c) and (self.c + self.b > self.a) and (self.a + self.c > self.b):
#             return 'Valid'
#         return 'Invalid'
#     def Side_Classification(self):
#         if (self.a + self.b <= self.c) or (self.c + self.b <= self.a) or (self.a + self.c <= self.b):
#             return 'Invalid'
#         if self.a == self.b == self.c:
#             return "Equilateral"
#         elif self.a == self.b != self.c:
#             return "Isosceles"
#         else:
#             return "Scalene"
#     def Angle_Classification(self):
#         if (self.a + self.b <= self.c) or (self.c + self.b <= self.a) or (self.a + self.c <= self.b):
#             return 'Invalid'
#         a = self.a
#         b = self.b
#         c = self.c
#         ac = ( ( (a <= c and b <= c) and(a ** 2 + b ** 2 > c ** 2) ) or ((c <= a and b <= a) and( c ** 2 + b ** 2 > a ** 2)) or ((a <= b and c <= b) and (a ** 2 +  c ** 2 >  b ** 2 )) )
#         ri = ( ((a <= c and b <= c) and(a ** 2 + b ** 2 == c ** 2) ) or ((c <= a and b <= a) and( c ** 2 + b ** 2 == a ** 2)) or ((a <= b and c <= b) and (a ** 2 +  c ** 2 ==  b ** 2 )) )
#         ob = ( ((a <= c and b <= c) and(a ** 2 + b ** 2 <  c ** 2) ) or ((c <= a and b <= a) and (c ** 2 + b ** 2  < a ** 2)) or ((a <= b and c <= b) and (a ** 2 +  c ** 2 <  b ** 2 )) )
#         if ac:
#             return 'Acute'
#         elif ri:
#             return 'Right'
#         elif ob:
#             return 'Obtuse'
#     def Area(self):
#         if (self.a + self.b <= self.c) or (self.c + self.b <= self.a) or (self.a + self.c <= self.b):
#             return 'Invalid'
#         a = self.a
#         b = self.b
#         c = self.c
#         s = ((float(a + b + c)) / 2)
#         asq = ((s) * (s-a) * (s-b) * (s-c))
#         area = float(math.sqrt(asq))
#         return area

###################

# def Twin_Primes(n,m):
#     primes = []
#     tprimes = []
#     for i in range(n,m+1):
#         if is_prime(i):
#             primes.append(i)
#         if (i-2 in primes) and (i in primes):
#             tprimes.append((i-2,i))
#     return tprimes

# print(Twin_Primes(5,50))

###################

# def Goldbach(n):
#     if n%2!=0 or n<=2:
#         return
#     prime = []
#     final = []
#     for i in range(2,n+1):
#         if is_prime(i):
#             prime.append(i)
#     l = len(prime)
#     for j in range(l):
#         if n-prime[j] in prime[j-1:]:
#             a = prime[j]
#             a = min(a, n-a)
#             b = max(a, n-a)
#             final.append((a,b))
#     return final

# print(Goldbach(26))

############################

# class Point:
#     def __init__(self, a=0,b=0):
#         self.x = a
#         self.y = b
#     def __str__(self):
#         return('('+str(self.x)+','+ str(self.y)+')')
#     def translate(self,deltax,deltay):
#         self.x += deltax
#         self.y += deltay
#     def odistance(self):
#         import math
#         d = math.sqrt(self.x*self.x + self.y*self.y)
#         return(d)
#     def __add__(self,p):
#         return(Point(self.x+p.x,self.y+p.y))

