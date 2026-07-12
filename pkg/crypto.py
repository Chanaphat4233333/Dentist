import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt_aes256(plaintext: str, key: str) -> bytes:
    key_bytes = key.encode('utf-8')
    
    data = plaintext.encode('utf-8')
    
    aesgcm = AESGCM(key_bytes)
    
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, data, None)
    
    return nonce + ciphertext
def decrypt_aes256(encrypted_data: bytes, key: bytes) -> str:
    aesgcm = AESGCM(key)
    
    nonce = encrypted_data[:12]
    ciphertext = encrypted_data[12:]
    
    decrypted_data = aesgcm.decrypt(nonce, ciphertext, None)
    
    return decrypted_data.decode('utf-8')