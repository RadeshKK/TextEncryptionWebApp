from Crypto.Cipher import DES

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt_DES(text, key):
    cipher = DES.new(key.encode(), DES.MODE_ECB)
    return cipher.encrypt(pad(text).encode()).hex()

def decrypt_DES(encrypted_text, key):
    cipher = DES.new(key.encode(), DES.MODE_ECB)
    return cipher.decrypt(bytes.fromhex(encrypted_text)).decode().strip()
