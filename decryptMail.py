from email.message import EmailMessage
from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Cipher import DES3
from Crypto.Cipher import Blowfish
from Crypto.Cipher import CAST
from Crypto.Cipher import ARC2
from Crypto.Cipher import Salsa20
from Crypto.Cipher import ChaCha20
from Crypto.Cipher import ARC4
from hashlib import md5
from binascii import hexlify
from binascii import unhexlify
import smtplib
import time
import imghdr

##CHOOSE ALGORITHM 
print('Choose the algorithm needed:\n\t1- AES\n\t2- DES\n\t3- 3DES\n\t4- Blowfish\n\t5- CAST120\n\t6- RC2\n\t7- SALSA20\n\t8- CHACHA20\n\t9- ARC4')
operation = input('Your Opinion: ')

if operation == '1':
    def dec(text):
        key = input('Enter your AES key: \n')
        start = time.time()
        key_hash = md5(key.encode('ascii')).digest()
        mode = AES.MODE_EAX
        cipher = AES.new(key_hash, mode, nonce=b'0') ##AES ALGORITHM
        ciphertext = cipher.decrypt(text)
        print("--- %s seconds ---" % ((time.time() - start)*1000))
        return ciphertext
    
if operation == '2':
    def dec(text):
        key = input('Enter your DES key (only 8 bytes): \n')
        start = time.time()
        key_hash = bytes(key, 'utf-8')
        mode = DES.MODE_EAX
        cipher = DES.new(key_hash, mode, nonce=b'0') ##DES ALGORITHM
        ciphertext = cipher.decrypt(text)
        print("--- %s seconds ---" % ((time.time() - start)*1000))
        return ciphertext
    
if operation == '3':
    def dec(text):
        key = input('Enter your DES3 key: \n')
        start = time.time()
        key_hash = md5(key.encode('ascii')).digest()
        mode = DES3.MODE_EAX
        cipher = DES3.new(key_hash, mode, nonce=b'0') ##3DES ALGORITHM
        ciphertext = cipher.decrypt(text)
        print("--- %s seconds ---" % ((time.time() - start)*1000))
        return ciphertext
    
if operation == '4':
    def dec(text):
        key = input('Enter your Blowfish key: \n')
        start = time.time()
        key_hash = md5(key.encode('ascii')).digest()
        mode = Blowfish.MODE_EAX
        cipher = Blowfish.new(key_hash, mode, nonce=b'0') ##BLOWFISH ALGORITHM
        ciphertext = cipher.decrypt(text)
        print("--- %s seconds ---" % ((time.time() - start)*1000))
        return ciphertext

if operation == '5':
    def dec(text):
        key = input('Enter your CAST120 key: \n')
        start = time.time()
        key_hash = md5(key.encode('ascii')).digest()
        mode = CAST.MODE_EAX
        cipher = CAST.new(key_hash, mode, nonce=b'0') ##CAST120 ALGORITHM
        ciphertext = cipher.decrypt(text)
        print("--- %s seconds ---" % ((time.time() - start)*1000))
        return ciphertext

if operation == '6':
    def dec(text):
        key = input('Enter your RC2 key: \n')
        start = time.time()
        key_hash = md5(key.encode('ascii')).digest()
        mode = ARC2.MODE_EAX
        cipher = ARC2.new(key_hash, mode, nonce=b'0') ##RC2 ALGORITHM
        ciphertext = cipher.decrypt(text)
        print("--- %s seconds ---" % ((time.time() - start)*1000))
        return ciphertext

if operation == '7':
    def dec(text):
        key = input('Enter your Salsa20 key: \n')
        start = time.time()
        key_hash = md5(key.encode('ascii')).digest()
        msg_nonce = text[:8]
        text = text[8:]
        cipher = Salsa20.new(key=key_hash, nonce=msg_nonce) ##SALSA20 ALGORITHM
        ciphertext = cipher.decrypt(text)
        print("--- %s seconds ---" % ((time.time() - start)*1000))
        return ciphertext    

if operation == '8':
    def dec(text):
        key = input('Enter your ChaCha20 key (only 32 bytes): \n')
        start = time.time()
        nonce = input('Enter your ChaCha20 nonce (only 12 bytes): \n')
        key_hash = bytes(key, 'utf-8')
        nonce_hash = bytes(nonce, 'utf-8')
        cipher = ChaCha20.new(key=key_hash, nonce=nonce_hash) ##CHACHA20 ALGORITHM
        ciphertext = cipher.decrypt(text)
        print("--- %s seconds ---" % ((time.time() - start)*1000))
        return ciphertext 

if operation == '9':
    def dec(text):
        key = input('Enter your ARC4 key: \n')
        start = time.time()
        key_hash = md5(key.encode('ascii')).digest()
        cipher = ARC4.new(key_hash) ##ARC4 ALGORITHM
        ciphertext = cipher.decrypt(text)
        print("--- %s seconds ---" % ((time.time() - start)*1000))
        return ciphertext

    
##DECRYPTION
print('Choose the decryption content:\n\t1- Text\n\t2- File')
operation1 = input('Your Opinion: ')

##TEXT ATTACHMENT
if operation1 == '1':
    mailcontent = input('Enter the mail content to be decrypted: \n')
    mailhex = unhexlify(mailcontent) #do both hex and string -> byte conversion
    ciphertext = dec(mailhex)
    print(mailcontent)
    print(mailhex)
    print(ciphertext)

##FILE ATTACHMENT 
if operation1 == '2':
    file_path = input('Enter the File Directory: \n')
    with open(file_path, 'rb') as input_file:
        file_bytes = input_file.read()
        new_file_bytes = dec(file_bytes)
    
    with open(file_path, 'wb') as output_file:
        output_file.write(new_file_bytes)
        print('Decryption done sucessfully!!')
