import random
import hashlib

def generate_primes():
    p = 23
    return p

def generate_keys():
    a_private = random.getrandbits(256)
    b_private = random.getrandbits(256)
    e_private = random.getrandbits(256)  
    return a_private, b_private, e_private

def compute_public_key(g, private_key, p):
    public_key = pow(g, private_key, p)
    return public_key

def compute_secret_key(public_key, private_key, p):
    secret_key = pow(public_key, private_key, p)
    return secret_key

def hash_key(key):
    hashed_key = hashlib.sha256(str(key).encode()).hexdigest()
    return hashed_key

def main():
    p = generate_primes()
    g = 2

    a_private, b_private, e_private = generate_keys() 

    A = compute_public_key(g, a_private, p)
    B = compute_public_key(g, b_private, p)
    E = compute_public_key(g, e_private, p)  

   
    A = E
    B = E

   
    s_alice = compute_secret_key(B, a_private, p)
    s_bob = compute_secret_key(A, b_private, p)
    s_eve = compute_secret_key(A, e_private, p)  

    
    hashed_s_alice = hash_key(s_alice)
    hashed_s_bob = hash_key(s_bob)
    hashed_s_eve = hash_key(s_eve)

    print("Clave secreta de Alice:", hashed_s_alice)
    print("Clave secreta de Bob:", hashed_s_bob)
    print("Clave secreta de Eve:", hashed_s_eve)

if __name__ == "__main__":
    main()
