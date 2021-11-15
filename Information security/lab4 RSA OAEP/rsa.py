import math


def encrypt(plaintext, public_key):
    N, e = public_key
    m = int.from_bytes(plaintext.encode('utf-8'), 'big')
    assert m < N
    c = pow(m, e, N)

    return c


def decrypt(ciphertext, private_key):
    p, q, d_p, d_q, q_inv = private_key
    c = ciphertext
    m1 = pow(c, d_p, p)
    m2 = pow(c, d_q, q)
    h = (q_inv * (m1 - m2)) % p
    m = (m2 + h * q) % (p * q)
    
    return m.to_bytes(math.ceil(m.bit_length()/8), 'big').decode("utf-8")
