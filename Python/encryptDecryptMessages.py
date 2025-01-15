"""
Author: Akshay Joshi
GitHub: https://github.com/ijoshi90
Creation Date: 02.12.24

Description: [Add a description here]
"""
from cryptography.fernet import Fernet
import sys

# Hardcoded key for educational purposes (keep this static for teaching)
# You can generate a new key for this example using: Fernet.generate_key()
KEY = b'zksXmMOEXMZ-ZBY_s5NlG03_PjX9iZmHWzMxYKiMzXg='

# Initialize Fernet cipher with the hardcoded key
cipher = Fernet(KEY)

def encode_message(message):
    """Encrypt the input message."""
    return cipher.encrypt(message.encode()).decode()

def decode_message(encoded_message):
    """Decrypt the input message."""
    return cipher.decrypt(encoded_message.encode()).decode()

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <encode|decode> <text>")
        sys.exit(1)

    mode = sys.argv[1].lower()
    text = sys.argv[2]

    try:
        if mode == "encode":
            print("Encoded message:", encode_message(text))
        elif mode == "decode":
            print("Decoded message:", decode_message(text))
        else:
            print("Invalid mode. Use 'encode' or 'decode'.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()