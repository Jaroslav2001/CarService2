import base64
import os
from hashlib import sha256, sha512
secret = 'secret123'
hash_secret = sha256(secret.encode()).digest()
hash_secret = base64.urlsafe_b64encode(hash_secret)


def get_hash(name: str):
    return sha512(hash_secret+name.encode()).hexdigest()
