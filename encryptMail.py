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
import imghdr
import time
import psutil


##CHOOSE ALGORITHM 
print('Choose the algorithm needed:\n\t1- AES\n\t2- DES\n\t3- 3DES\n\t4- Blowfish\n\t5- CAST120\n\t6- RC2\n\t7- SALSA20\n\t8- CHACHA20\n\t9- ARC4')
operation = input('Your Opinion: ')

if operation == '1':
    def enc(text):
        key = input('Enter your AES key: \n')
        start = time.time()
        key_hash = md5(key.encode('ascii')).digest()
        mode = AES.MODE_EAX
        cipher = AES.new(key_hash, mode, nonce=b'0') ##AES ALGORITHM
        ciphertext = cipher.encrypt(text)
        print("--- %s seconds ---" % ((time.time() - start)*1000))
        print("CPU % used:", psutil.cpu_percent())
        #print(psutil.virtual_memory())  # physical memory usage
        print('memory % used:', psutil.virtual_memory()[2])
        print('disk % used:', psutil.disk_usage('/'))
        #print('disk % used:', psutil.disk_usage()[3])
        return ciphertext
    
if operation == '2':
    def enc(text):
        key = input('Enter your DES key (only 8 bytes): \n')
        start = time.time()
        key_hash = bytes(key, 'utf-8')
        mode = DES.MODE_EAX
        cipher = DES.new(key_hash, mode, nonce=b'0') ##DES ALGORITHM
        ciphertext = cipher.encrypt(text)
        print("--- %s seconds ---" % ((time.time() - start)*1000))
        print("CPU % used:", psutil.cpu_percent())
        #print(psutil.virtual_memory())  # physical memory usage
        print('memory % used:', psutil.virtual_memory()[2])
        print('disk % used:', psutil.disk_usage('/'))
        #print('disk % used:', psutil.disk_usage()[3])
        return ciphertext
    
if operation == '3':
    def enc(text):
        key = input('Enter your DES3 key: \n')
        start = time.time()
        key_hash = md5(key.encode('ascii')).digest()
        mode = DES3.MODE_EAX
        cipher = DES3.new(key_hash, mode, nonce=b'0') ##3DES ALGORITHM
        ciphertext = cipher.encrypt(text)
        print("--- %s seconds ---" % ((time.time() - start)*1000))
        print("CPU % used:", psutil.cpu_percent())
        #print(psutil.virtual_memory())  # physical memory usage
        print('memory % used:', psutil.virtual_memory()[2])
        print('disk % used:', psutil.disk_usage('/'))
        #print('disk % used:', psutil.disk_usage()[3])
        return ciphertext
    
if operation == '4':
    def enc(text):
        key = input('Enter your Blowfish key: \n')
        start = time.time()
        key_hash = md5(key.encode('ascii')).digest()
        mode = Blowfish.MODE_EAX
        cipher = Blowfish.new(key_hash, mode, nonce=b'0') ##BLOWFISH ALGORITHM
        ciphertext = cipher.encrypt(text)
        print("--- %s seconds ---" % ((time.time() - start)*1000))
        print("CPU % used:", psutil.cpu_percent())
        #print(psutil.virtual_memory())  # physical memory usage
        print('memory % used:', psutil.virtual_memory()[2])
        print('disk % used:', psutil.disk_usage('/'))
        #print('disk % used:', psutil.disk_usage()[3])
        return ciphertext

if operation == '5':
    def enc(text):
        key = input('Enter your CAST120 key: \n')
        start = time.time()
        key_hash = md5(key.encode('ascii')).digest()
        mode = CAST.MODE_EAX
        cipher = CAST.new(key_hash, mode, nonce=b'0') ##CAST120 ALGORITHM
        ciphertext = cipher.encrypt(text)
        print("--- %s seconds ---" % ((time.time() - start)*1000))
        print("CPU % used:", psutil.cpu_percent())
        #print(psutil.virtual_memory())  # physical memory usage
        print('memory % used:', psutil.virtual_memory()[2])
        print('disk % used:', psutil.disk_usage('/'))
        #print('disk % used:', psutil.disk_usage()[3])
        return ciphertext

if operation == '6':
    def enc(text):
        key = input('Enter your RC2 key: \n')
        start = time.time()
        key_hash = md5(key.encode('ascii')).digest()
        mode = ARC2.MODE_EAX
        cipher = ARC2.new(key_hash, mode, nonce=b'0') ##RC2 ALGORITHM
        ciphertext = cipher.encrypt(text)
        print("--- %s seconds ---" % ((time.time() - start)*1000))
        print("CPU % used:", psutil.cpu_percent())
        #print(psutil.virtual_memory())  # physical memory usage
        print('memory % used:', psutil.virtual_memory()[2])
        print('disk % used:', psutil.disk_usage('/'))
        #print('disk % used:', psutil.disk_usage()[3])
        return ciphertext

if operation == '7':
    def enc(text):
        key = input('Enter your Salsa20 key: \n')
        start = time.time()
        key_hash = md5(key.encode('ascii')).digest()
        cipher = Salsa20.new(key=key_hash) ##SALSA20 ALGORITHM
        ciphertext = cipher.nonce + cipher.encrypt(text)
        print("--- %s seconds ---" % ((time.time() - start)*1000))
        print("CPU % used:", psutil.cpu_percent())
        #print(psutil.virtual_memory())  # physical memory usage
        print('memory % used:', psutil.virtual_memory()[2])
        print('disk % used:', psutil.disk_usage('/'))
        #print('disk % used:', psutil.disk_usage()[3])
        return ciphertext    

if operation == '8':
    def enc(text):
        key = input('Enter your ChaCha20 key (only 32 bytes): \n')
        start = time.time()
        nonce = input('Enter your ChaCha20 nonce (only 12 bytes): \n')
        key_hash = bytes(key, 'utf-8')
        nonce_hash = bytes(nonce, 'utf-8')
        cipher = ChaCha20.new(key=key_hash, nonce=nonce_hash) ##CHACHA20 ALGORITHM
        ciphertext = cipher.encrypt(text)
        print("--- %s seconds ---" % ((time.time() - start)*1000))
        print("CPU % used:", psutil.cpu_percent())
        #print(psutil.virtual_memory())  # physical memory usage
        print('memory % used:', psutil.virtual_memory()[2])
        print('disk % used:', psutil.disk_usage('/'))
        #print('disk % used:', psutil.disk_usage()[3])
        return ciphertext 

if operation == '9':
    def enc(text):
        key = input('Enter your ARC4 key: \n')
        start = time.time()
        key_hash = md5(key.encode('ascii')).digest()
        cipher = ARC4.new(key_hash) ##ARC4 ALGORITHM
        ciphertext = cipher.encrypt(text)
        print("--- %s seconds ---" % ((time.time() - start)*1000))
        print("CPU % used:", psutil.cpu_percent())
        #print(psutil.virtual_memory())  # physical memory usage
        print('memory % used:', psutil.virtual_memory()[2])
        print('disk % used:', psutil.disk_usage('/'))
        #print('disk % used:', psutil.disk_usage()[3])
        return ciphertext
    
##ENCRYPTION
def send_email(receiver, subject, body):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login('tamilcipher@gmail.com', 'Abcdefgh1.')
    email = EmailMessage()
    email['From'] = 'tamilcipher@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    body = body

    ##TEXT ATTACHMENT
    text = bytes(body, 'utf-8')
    ciphertext = enc(text)
    print('Encrypted Text: \n',ciphertext)
    print('Encrypted Text as byte: \n',hexlify(ciphertext))
    print('Encrypted Text as string: \n',str(hexlify(ciphertext), "utf-8"))
    encbody = str(hexlify(ciphertext), "utf-8")
    email.set_content(encbody)

    ##FILE ATTACHMENT
    n = int(input("Enter number of attachments (if any): \n"))
    files = list(map(str,input("\nEnter the Filename(without space) seperated by spaces : \n").strip().split()))[:n]
    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_bytes = enc(file_data)      
            file_name = f.name
        email.add_attachment(file_bytes, maintype='application', subtype='octet-stream', filename=file_name)

    
    server.send_message(email)
    print('Mail sent sucessfully!!')


receiver = input('Enter the Receiver Mail : \n')
subject = input('Enter the Subject of the Mail : \n')
##receiver = 'prave.anand124@gmail.com'
##subject = 'Encrypt mail with attachment'
body = input('Enter the Body of the Mail : \n')

send_email(receiver, subject, body)
