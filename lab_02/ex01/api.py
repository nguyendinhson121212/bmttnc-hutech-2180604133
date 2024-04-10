from flask import Flask, request, jsonify
#from cipher.caesar import CaesarCipher
#from cipher.vigenere import VigenereCipher
#from cipher.railfence import RailFenceCipher
#from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher


app = Flask(__name__)

#TRANSPOSITION CIPHER ALGORITHM
transposition_cipher = TranspositionCipher()


 # @app.route("/api/playfair/creatematrix", methods=["POST"])
 # def playfair_creatematrix():
   # data = request.json
    # plain_text = data['plain_text']
   # key = data['key']
   # playfair_matrix = playfair_cipher.create_playfair_matrix(key)
   # return jsonify({'playfair_matrix': playfair_matrix})

@app.route('/api/transposition/encrypt', methods=["POST"])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text  =   transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route("/api/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text  =   transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})
   
#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    