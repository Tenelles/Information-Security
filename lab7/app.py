import random
import string

def generate_key(length):
	return ''.join(random.choice(string.ascii_letters + string.digits) \
					 			for _ in range(length))
def to_hex(input_string):
	return ' '.join('{:02x}'.format(ord(symbol)) \
								for symbol in input_string)
def beuatify(text):
	return "{} | {}".format(text, to_hex(text))

def single_gamming(message, key):
	return ''.join(chr(ord(m) ^ ord(k)) for m, k in zip(message, key))

def decrypt(encrypted, key):
	return single_gamming(encrypted, key)

def find_key(message, encrypted):
	return single_gamming(message, encrypted)

message = input("Enter message to encrypt: ")

key = generate_key(len(message))
print("Key:", beuatify(key))

encrypted = single_gamming(message, key)
print("Encrypted message:", beuatify(encrypted))

print("Decrypted message:", decrypt(encrypted, key))

wrong_message = "Hello earth!"
wrong_key = find_key(encrypted, wrong_message)
print("\nKey:", beuatify(wrong_key))

print("Decrypted wrong message:", decrypt(encrypted, wrong_key))