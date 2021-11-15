import rsa
import oaep
from generate_keys import generate_keys
from time import time


if __name__ == '__main__':
    plaintext = "Message to encrypt"
    print(f'Plaintext: {plaintext}')

    start = time()
    public_key, private_key = generate_keys(768)
    print(f'Keys generated in {time() - start} s\n')

    print('\t\tRSA')
    start = time()
    c = rsa.encrypt(plaintext, public_key)
    encr_time = time()
    print(f'cipher: {c}')
    m = rsa.decrypt(c, private_key)
    print(f'decrypted: {m}')
    print(f'\t\tEncryption: {encr_time-start} s, Decryption: {time()-encr_time} s\n\n')


    print('\t\tOAEP')
    start = time()
    c = oaep.encrypt(plaintext, public_key)
    encr_time = time()
    print(f'cipher: {c}')
    m = oaep.decrypt(c, private_key)
    print(f'decrypted: {m}')
    print(f'\t\tEncryption: {encr_time-start} s, Decryption: {time()-encr_time} s\n\n')
