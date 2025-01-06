from PIL import Image
import numpy as np

# Function to encode a message in an image
def encode_message(image_path, message):
    image = Image.open(image_path)
    image_data = np.array(image)
    
    # Convert message to binary
    binary_message = ''.join(format(ord(i), '08b') for i in message) + '1111111111111110'  # Adding delimiter
    
    data_index = 0
    for row in range(image_data.shape[0]):
        for col in range(image_data.shape[1]):
            pixel = image_data[row, col]
            for color in range(3):
                if data_index < len(binary_message):
                    # Replace LSB (Least Significant Bit) of each color with the message bits
                    pixel[color] = (pixel[color] & 0xFE) | int(binary_message[data_index])
                    data_index += 1
            image_data[row, col] = pixel
    
    # Save the new image with encoded message
    encoded_image_path = "uploads/encoded_image.png"
    encoded_image = Image.fromarray(image_data)
    encoded_image.save(encoded_image_path)
    
    return encoded_image_path

# Function to decode the hidden message from an image
def decode_message(image_path):
    image = Image.open(image_path)
    image_data = np.array(image)
    
    binary_message = ''
    for row in range(image_data.shape[0]):
        for col in range(image_data.shape[1]):
            pixel = image_data[row, col]
            for color in range(3):
                # Get the LSB (Least Significant Bit) from each color channel
                binary_message += str(pixel[color] & 1)
    
    # Look for delimiter to stop decoding
    delimiter = '1111111111111110'
    end_index = binary_message.find(delimiter)
    
    if end_index != -1:
        binary_message = binary_message[:end_index]  # Remove extra bits after delimiter
    
    # Divide the binary message into chunks of 8 bits and convert to text
    message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
    
    return message
