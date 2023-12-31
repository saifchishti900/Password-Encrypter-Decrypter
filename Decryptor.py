"""This code is written by the Author Saif Chishti. It can be used by anyone who have access to it."""

# Decrypts the base64 encoded texts
# Import required libraries
import base64


def DecryptPassword(encoded):
    decoded_bytes = base64.b64decode(encoded)
    decoded_password = decoded_bytes.decode()
    print(decoded_password)


encoded_pass = input("Enter the base64 encoded password: ")
DecryptPassword(encoded_pass)
