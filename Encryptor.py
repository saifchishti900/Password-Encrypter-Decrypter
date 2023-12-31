"""This code is written by the Author Saif Chishti. It can be used by anyone who have access to it."""

# Uses base64 encoding to encrypt the text
# Import required libraries
import base64


def EncryptPassword(password):
    encoded_pass = base64.b64encode(password.encode())
    print(encoded_pass)


user_password = input("Enter you password to encrypt: ")
EncryptPassword(user_password)
