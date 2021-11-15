import math
import os
from hashlib import sha256

hash_func = lambda x: sha256(x).digest()
hash_len = 32


def xor_bytes(bytes1, bytes2):
    assert len(bytes1) == len(bytes2)
    return bytes(a ^ b for (a, b) in zip(bytes1, bytes2))


def mgf1(bytes, length):
    counter = 0
    output = b''
    while len(output) < length:
        input_bytes = bytes + counter.to_bytes(4, 'big')
        output += hash_func(input_bytes)
        counter += 1
    return output[:length]


def encrypt(plaintext, public_key, label=b''):
    plaintext = plaintext.encode('utf-8')
    N, e = public_key
    n = math.ceil(N.bit_length() / 8)
    m_len = len(plaintext)
    assert m_len <= n - 2 * hash_len - 2

    label_hash = hash_func(label)
    zero_padding = b'\x00' * (n - m_len - 2 * hash_len - 2)
    db = label_hash + zero_padding + b'\x01' + plaintext
    seed = os.urandom(hash_len)

    db_mask = mgf1(seed, n - hash_len - 1)
    masked_db = xor_bytes(db, db_mask)
    seed_mask = mgf1(masked_db, hash_len)
    masked_seed = xor_bytes(seed, seed_mask)

    em = b'\x00' + masked_seed + masked_db
    m = int.from_bytes(em, 'big')
    c = pow(m, e, N)
    return c


def decrypt(ciphertext, private_key, label=b''):
    p, q, d_p, d_q, q_inv = private_key
    N = p * q
    k = math.ceil(N.bit_length() / 8)

    c = ciphertext
    m1 = pow(c, d_p, p)
    m2 = pow(c, d_q, q)
    h = (q_inv * (m1 - m2)) % p
    m = (m2 + h * q) % (p * q)
    em = m.to_bytes(k, 'big')

    label_hash = hash_func(label)
    masked_db = em[-(k - hash_len - 1):]
    masked_seed = em[-(k - 1): -(k - hash_len - 1)]

    seed_mask = mgf1(masked_db, hash_len)
    seed = xor_bytes(masked_seed, seed_mask)
    db_mask = mgf1(seed, k - hash_len - 1)
    db = xor_bytes(masked_db, db_mask)

    decrypted_label_hash = db[:hash_len]
    assert label_hash == decrypted_label_hash

    i = hash_len
    while db[i] == 0:
        i += 1
    plaintext = db[i + 1:]
    return plaintext.decode("utf-8")
