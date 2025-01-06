from flask import Flask, render_template, request, send_file, jsonify
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from PIL import Image
import io
import base64
import secrets

app = Flask(__name__)

# AES Encryption
def encrypt_message(message, password):
    salt = secrets.token_bytes(16)  # Generate a random salt
    iv = secrets.token_bytes(16)    # Generate a random IV
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(message.encode()) + encryptor.finalize()
    # Prepend salt and IV to the encrypted message for later decryption
    return salt + iv + encrypted_message


def decrypt_message(encrypted_message, password):
    # Extract salt and IV
    salt = encrypted_message[:16]
    iv = encrypted_message[16:32]
    encrypted_data = encrypted_message[32:]
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(encrypted_data) + decryptor.finalize()
    return decrypted_message.decode()


# Image Steganography
import math

# Function to check if a number is a power of 2
def isPowerOfTwo(n):
    return (math.ceil(math.log2(n)) == math.floor(math.log2(n)))

# Embed message using mathematical methods
def embed_message(image_file, message):
    image = Image.open(image_file)
    encoded_image = image.copy()
    width, height = image.size
    message += "<<<END>>>"  # Marker for message end
    message_bits = ''.join([format(ord(char), "08b") for char in message])
    data_index = 0

    # Loop through each pixel and apply the mathematical encoding
    for x in range(width):
        for y in range(height):
            pixel = list(encoded_image.getpixel((x, y)))
            for n in range(3):  # Loop over R, G, B channels
                if data_index < len(message_bits):
                    # Apply mathematical method to modify the pixel value
                    pixel[n] = int(pixel[n] + (int(message_bits[data_index]) * math.pow(2, 5)))  # Adjust pixel value using a power of 2
                    data_index += 1
            encoded_image.putpixel((x, y), tuple(pixel))
            if data_index >= len(message_bits):
                break
        if data_index >= len(message_bits):
            break

    # Save the modified image to a byte stream
    output_image = io.BytesIO()
    encoded_image.save(output_image, format="PNG")
    output_image.seek(0)
    return output_image



# Extract message using the mathematical method
def extract_message(image_file):
    image = Image.open(image_file)
    width, height = image.size
    message_bits = []

    # Loop through each pixel to retrieve the encoded message
    for x in range(width):
        for y in range(height):
            pixel = list(image.getpixel((x, y)))
            for n in range(3):  # Loop over R, G, B channels
                # Reverse the mathematical operation to extract the bit
                message_bits.append((pixel[n] // math.pow(2, 5)) % 2)  # Use modulus to retrieve the bit

    # Convert the binary message to characters
    message_bytes = [message_bits[i:i + 8] for i in range(0, len(message_bits), 8)]
    message = ''.join([chr(int(''.join(map(str, byte)), 2)) for byte in message_bytes])

    # Return the message, excluding the end marker
    return message.split("<<<END>>>")[0]

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encode", methods=["POST"])
def encode():
    message = request.form["message"]
    password = request.form["password"]
    image = request.files["image"]
    
    encrypted_message = encrypt_message(message, password)
    encoded_image = embed_message(image, base64.b64encode(encrypted_message).decode())
    
    encoded_image.seek(0)
    encoded_image_base64 = base64.b64encode(encoded_image.read()).decode("utf-8")
    return render_template("index.html", encoded_image=encoded_image_base64, message=None)

@app.route("/decode", methods=["POST"])
def decode():
    password = request.form["password"]
    encoded_image = request.files["encoded_image"]
    
    try:
        encrypted_message = extract_message(encoded_image)
        decrypted_message = decrypt_message(base64.b64decode(encrypted_message), password)
    except Exception:
        return render_template("index.html", error="Invalid password or corrupted data!", message=None, encoded_image=None)
    
    return render_template("index.html", message=decrypted_message, encoded_image=None)

if __name__ == "__main__":
    app.run(debug=True)
