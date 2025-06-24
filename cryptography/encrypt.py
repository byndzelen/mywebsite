#!/usr/bin/env python3

from cryptography.fernet import Fernet
import base64
import os

# Generate & store key
def generate_key(password: str):
    return base64.urlsafe_b64encode(password.encode('utf-8').ljust(32, b'\0'))

# Encrypt file
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(file_path + ".enc", 'wb') as f:
        f.write(encrypted)
    print(f"File encrypted: {file_path}.enc")

# Decrypt file
def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        data = f.read()
    decrypted = fernet.decrypt(data)
    output_path = file_path.replace(".enc", "")
    with open(output_path, 'wb') as f:
        f.write(decrypted)
    print(f"File decrypted: {output_path}")

# Usage
password = input("Enter password: ")
key = generate_key(password)

choice = input("Encrypt or Decrypt? (e/d): ")
file_path = input("File path: ")

if choice.lower() == 'e':
    encrypt_file(file_path, key)
elif choice.lower() == 'd':
    decrypt_file(file_path, key)
else:
    print("Invalid choice")

