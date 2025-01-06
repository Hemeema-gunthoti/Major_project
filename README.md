# Stega Vault

### **What is Steganography?**
Steganography is the practice of hiding a secret message within a non-secret medium, such as an image, audio file, or text, in a way that prevents detection. Unlike cryptography, which focuses on making the content unreadable, steganography aims to make the presence of the hidden data undetectable.

---

### **Why is Steganography Important?**
- **Confidentiality:** It helps maintain secrecy by concealing the very existence of the message.
- **Avoiding Suspicion:** Hidden data does not attract attention, making it harder for attackers to notice or intercept.
- **Dual-Layer Security:** When combined with cryptography, it provides a second layer of protection.
- **Applications:** Used in digital watermarking, secure communication, and copyright protection.

---

### **What is Cryptography?**
Cryptography is the science of encrypting data to protect it from unauthorized access. It converts plaintext into ciphertext using mathematical algorithms and a key, ensuring that only authorized parties can decrypt and understand the data.

---

### **How We Merged Steganography and Cryptography**
In our project, we combined the strengths of both techniques:
1. **Cryptography:** The secret message is encrypted using the AES (Advanced Encryption Standard) algorithm, ensuring that even if the hidden data is discovered, it cannot be read without the decryption key.
2. **Steganography:** The encrypted message is embedded into an image using a mathematical embedding method (replacing traditional Least Significant Bit (LSB) manipulation). This ensures that the encrypted data is hidden in plain sight.

By merging both:
- The presence of the data is concealed (steganography).
- The content of the data is protected (cryptography).

---

### **Algorithms Used**
1. **AES Encryption (Cryptography):**
   - **Purpose:** Encrypts the message to prevent unauthorized access.
   - **Process:**
     1. A random salt and IV (Initialization Vector) are generated for additional security.
     2. The key is derived using PBKDF2HMAC with a password and salt.
     3. The message is encrypted using AES in CFB (Cipher Feedback) mode.
   - **Benefits:**
     - Strong encryption standard widely used in secure communications.
     - Resistant to brute-force attacks.

2. **Mathematical Embedding (Steganography):**
   - **Purpose:** Embeds the encrypted message into the image without altering its visual quality.
   - **Process:**
     1. The encrypted message is converted into binary format.
     2. A mathematical method is used to calculate the embedding positions in the image, avoiding a simple LSB replacement.
     3. The message bits are inserted into the pixel values of the image.
   - **Benefits:**
     - Avoids suspicion as the image remains visually unchanged.
     - More secure than traditional LSB methods.

---

### **Benefits of Merging Both Technologies**
1. **Enhanced Security:** Even if the hidden data is discovered, encryption ensures it remains unreadable.
2. **Dual-Layer Protection:** Provides both obfuscation (steganography) and encryption (cryptography).
3. **Resilience to Attacks:** Protects against steganalysis and cryptanalysis when implemented correctly.
4. **Wide Applications:** Useful in secure communications, digital forensics, and protecting intellectual property.

---

### **List of Technologies Used**
1. **Python:** Programming language for implementing cryptography and steganography algorithms.
2. **Flask:** Web framework for building the application interface.
3. **Pillow (PIL):** Library for image processing.
4. **Cryptography Library:** Provides tools for AES encryption and decryption.
5. **HTML/CSS/JavaScript:** For the user interface of the web application.
6. **Git:** Version control system for managing code.

---

### **Why Should We Use Steganography + Cryptography?**
1. **Complementary Strengths:** Steganography hides the existence of data, while cryptography protects its content.
2. **Robust Security:** Combining both makes it significantly harder for attackers to detect, extract, or decrypt the data.
3. **Practical Applications:** Ideal for secure data transfer, protecting sensitive information, and copyright enforcement.
4. **Avoids Detection:** Unlike cryptography alone, which might attract attention, steganography ensures that the communication remains covert.

By using both steganography and cryptography, we achieve a highly secure and reliable system for protecting sensitive information.
