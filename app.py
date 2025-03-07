from flask import Flask, render_template, request, jsonify
from encryption.aes import encrypt_AES, decrypt_AES
from encryption.des import encrypt_DES, decrypt_DES
from encryption.rsa import encrypt_RSA, decrypt_RSA

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    text = data['text']
    method = data['method']
    key = data.get('key', '')

    if method == 'AES':
        encrypted_text = encrypt_AES(text, key)
    elif method == 'DES':
        encrypted_text = encrypt_DES(text, key)
    elif method == 'RSA':
        encrypted_text = encrypt_RSA(text)
    else:
        return jsonify({'error': 'Invalid encryption method'}), 400

    return jsonify({'encrypted_text': encrypted_text})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    encrypted_text = data['encrypted_text']
    method = data['method']
    key = data.get('key', '')

    if method == 'AES':
        decrypted_text = decrypt_AES(encrypted_text, key)
    elif method == 'DES':
        decrypted_text = decrypt_DES(encrypted_text, key)
    elif method == 'RSA':
        decrypted_text = decrypt_RSA(encrypted_text)
    else:
        return jsonify({'error': 'Invalid decryption method'}), 400

    return jsonify({'decrypted_text': decrypted_text})

if __name__ == "__main__":
    app.run(debug=True)
