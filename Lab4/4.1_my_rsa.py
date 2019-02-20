import random
def extended_euclid( a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_euclid(b % a, a)
        return (g, y - (b // a) * x, x)

def modular_inv( b, n):
    g, x, y = extended_euclid(b, n)
    if g == 1:
        return x % n

def e_selector(phi_n):
    e_values=[]
    for i in range(2,phi_n+1):
        gcd,x,y=extended_euclid(phi_n,i)
        if gcd==1:
            e_values.append(i)
    return random.choice(e_values)

def encrypt(msg,e,n):
    c = msg ** e
    return c % n

def decrypt( msg,d,n):
    m = msg ** d
    return m % n

def main():
    p = 11
    q = 13
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 7
    e_selector(phi_n)
    d = modular_inv(e, phi_n)
    m = 80
    print 'Message : ', m,'\n'
    c = encrypt(m,e,n)
    m = decrypt(c,d,n)
    print 'Public key :',e,n
    print 'Encrypted : ', c
    print 'Private key :',d,n
    print 'Decrypted : ', m


if __name__== "__main__":
    main()