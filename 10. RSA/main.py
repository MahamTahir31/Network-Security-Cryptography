import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#2 random prime numbers
p = 13
q = 11
n = p * q  
phi = (p - 1) * (q - 1)  

# public key
e = 7
while e < phi:
    if gcd(e, phi) == 1:
        break
    else:
        e += 1

# private key
d = pow(e, -1, phi)

message = 9
c = pow(message, e, n) 
m = pow(c, d, n)

print("Original Message =", message)
print("p =", p)
print("q =", q)
print("n = pq =", n)
print("phi =", phi)
print("e =", e)
print("d =", d)
print("Encrypted message =", c)
print("Decrypted message =", m)
