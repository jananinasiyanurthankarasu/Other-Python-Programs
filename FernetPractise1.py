#fernet practise1

from cryptography.fernet import Fernet

key = Fernet.generate_key()
fer = Fernet(key)

msg = b"Hello world"

encrypted_msg = fer.encrypt(msg)

decrypted_msg = fer.decrypt(encrypted_msg)

print(encrypted_msg)

print(decrypted_msg)