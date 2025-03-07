from Crypto.Cipher import AES
import base64

def pad(text):
    return text + (16 - len(text) % 16) * ' '

def encrypt_AES(text, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(pad(text).encode())).decode()

def decrypt_AES(encrypted_text, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    return cipher.decrypt(base64.b64decode(encrypted_text)).decode().strip()
