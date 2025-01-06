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

   Here is a clear list of the libraries used in your project, along with explanations of their purpose:

---

### **1. Flask**
- **Purpose:** Flask is a lightweight web framework used to create web applications.
- **Role in the Project:**
  - Manages HTTP requests and responses.
  - Provides routes for encoding and decoding operations.
  - Serves the user interface (HTML templates) and handles form submissions.
- **Why Use Flask?**
  - Easy to use and configure for small to medium-sized projects.
  - Allows rapid development of web applications.

---

### **2. Cryptography**
- **Purpose:** A library for implementing cryptographic algorithms securely.
- **Role in the Project:**
  - Provides AES (Advanced Encryption Standard) for encrypting and decrypting messages.
  - Includes PBKDF2HMAC (Password-Based Key Derivation Function 2) for generating secure keys from passwords.
  - Manages secure handling of salts, initialization vectors (IV), and encryption processes.
- **Why Use Cryptography?**
  - Implements modern, secure cryptographic primitives.
  - Simplifies encryption tasks while ensuring best practices are followed.

---

### **3. Pillow (PIL Fork)**
- **Purpose:** A Python library for image processing.
- **Role in the Project:**
  - Opens, manipulates, and saves images.
  - Embeds the encrypted message into the image.
  - Extracts the hidden message from the image.
- **Why Use Pillow?**
  - Easy-to-use functions for image manipulation.
  - Supports a wide range of image formats like PNG, JPEG, BMP, etc.

---

### **4. Base64**
- **Purpose:** A standard library module for encoding and decoding data in Base64 format.
- **Role in the Project:**
  - Encodes the encrypted message into a format suitable for embedding in an image.
  - Decodes the extracted data back into its original binary format.
- **Why Use Base64?**
  - Converts binary data into a text format that is easier to embed and transmit.

---

### **5. Secrets**
- **Purpose:** A standard library module for generating secure random numbers and data.
- **Role in the Project:**
  - Generates cryptographically secure random values for the salt and IV used in encryption.
- **Why Use Secrets?**
  - Provides a secure way to generate random values, essential for cryptographic security.

---

### **6. io**
- **Purpose:** A standard library module for handling in-memory file-like objects.
- **Role in the Project:**
  - Temporarily stores the modified image in memory before saving or sending it to the user.
- **Why Use io?**
  - Eliminates the need for intermediate file storage on disk, improving efficiency.

---

### **7. HTML/CSS/JavaScript**
- **Purpose:** Technologies for building the user interface of the web application.
- **Role in the Project:**
  - HTML: Structures the content of the web pages.
  - CSS: Styles the web pages for a better user experience.
  - JavaScript: Adds interactivity to the web pages, such as previewing images or validating form inputs.
- **Why Use HTML/CSS/JavaScript?**
  - Essential for creating a user-friendly and visually appealing interface.

---

### **8. Git**
- **Purpose:** A version control system for tracking changes in code and collaborating with others.
- **Role in the Project:**
  - Manages the project's source code and ensures version history is maintained.
  - Facilitates collaboration and code sharing through GitHub.
- **Why Use Git?**
  - Provides a reliable way to manage code changes and resolve conflicts.

---

### **Summary of Libraries and Tools**
| **Library/Tool**      | **Purpose**                                    | **Why Use It?**                                                  |
|------------------------|-----------------------------------------------|------------------------------------------------------------------|
| Flask                 | Web framework                                 | For handling HTTP requests and serving the web app.             |
| Cryptography          | Cryptographic operations                      | For AES encryption and secure key derivation.                   |
| Pillow                | Image processing                              | For embedding and extracting messages from images.              |
| Base64                | Data encoding                                 | For converting binary data into text format.                    |
| Secrets               | Secure random data generation                 | For generating salt and IV for encryption.                      |
| io                    | In-memory file handling                       | For temporarily storing images without saving to disk.          |
| HTML/CSS/JavaScript   | Front-end development                         | For creating and styling the web application's user interface.  |
| Git                   | Version control                               | For managing code and collaborating effectively.                |

By using these libraries and tools, your project achieves secure, efficient, and user-friendly functionality for steganography and cryptography.

---

### **Why Should We Use Steganography + Cryptography?**
1. **Complementary Strengths:** Steganography hides the existence of data, while cryptography protects its content.
2. **Robust Security:** Combining both makes it significantly harder for attackers to detect, extract, or decrypt the data.
3. **Practical Applications:** Ideal for secure data transfer, protecting sensitive information, and copyright enforcement.
4. **Avoids Detection:** Unlike cryptography alone, which might attract attention, steganography ensures that the communication remains covert.

By using both steganography and cryptography, we achieve a highly secure and reliable system for protecting sensitive information.
