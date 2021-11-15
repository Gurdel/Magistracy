import math
import random


def generate_keys(num_bits):
    p = generate_prime_number(num_bits)
    q = generate_prime_number(num_bits)
    N = p * q
    phi_N = (p - 1) * (q - 1)
    e = find_e(phi_N)
    d = extended_euclid(e, phi_N)
    d_p = d % (p - 1)
    d_q = d % (q - 1)
    q_inv = extended_euclid(q, p)

    return (N, e), (p, q, d_p, d_q, q_inv)


def miller_rabin(n, k):
    if n < 2:
        return False
    if n in {2, 3}:
        return True

    d = n - 1
    r = 0
    while d % 2 == 0:
        r += 1
        d = d // 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True


def generate_prime_number(num_bits, k=20):
    assert num_bits >= 2

    l, h = 2 ** (num_bits - 1), 2 ** num_bits - 1
    while True:
        a = random.randint(l, h)
        if miller_rabin(a, k):
            return a


def find_e(phi_n):
    while True:
        e = random.randint(3, phi_n - 1)
        if math.gcd(e, phi_n) == 1:
            return e


def extended_euclid(a, b):
    buf = b
    x, d = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x, d = d - q * x, x
    if d < 0:
        d += buf
    
    return d
