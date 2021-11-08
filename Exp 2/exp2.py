from math import sqrt

def is_prime(n):
    prime_flag = 0
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    return False





def diffie_hellman():
    p = int(input('Enter the prime number: '))
    if not is_prime(p):
        p = int(input("Number not prime\nEnter again: "))

    g = int(input('Enter the generator(Primitive root of P): '))
    

    x = int(input('\nEnter the Secret x: '))
    y = int(input('Enter the Secret y: '))
    X = int(pow(g,x,p))
    Y = int(pow(g,y,p))
    ka = int(pow(Y,x,p))
    kb = int(pow(X,y,p))

    print('\nSecret key K1 :',ka)
    print('Secret Key K2 :',kb)

if __name__  == '__main__':
    diffie_hellman()

# 444179302003117
# 7353133049
# 4530
# 2570