from hashlib import sha256
from random import randint


proof = ""

for _ in range(10):
    i = 0
    proof += "0"
    while True:
        i += 1
        hash = randint(10000000000000000000000000000000000,
                        99999999999999999999999999999999999)
        hash = sha256(str(hash).encode()).hexdigest()
        if hash.startswith(proof):
            print(i, proof, hash)
            break