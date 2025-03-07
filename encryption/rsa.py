from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

def encrypt_RSA(text):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    return base64.b64encode(cipher.encrypt(text.encode())).decode()

def decrypt_RSA(encrypted_text):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    return cipher.decrypt(base64.b64decode(encrypted_text)).decode()
