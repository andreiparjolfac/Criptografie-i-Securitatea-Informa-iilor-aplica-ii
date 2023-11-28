#Exercitii Propuse 1.3

def encrypt_cezar(key,plaintext):
    plaintext = plaintext.lower()
    ciphertext = ""

    for letter in plaintext:
        if not (ord(letter)>=ord('a') and ord (letter) <= ord('z')):
            ciphertext+=' '
        x = ord(letter) - ord('a')
        x = chr((x+key) % 26 + ord('a'))
        ciphertext +=x 

    print("key: "+str(key)+" "+ciphertext.upper())

def decipher_cezar(key,ciphertext):
    encrypt_cezar(-key,ciphertext)

def brute_f_cezar_decryptor(ciphertext):
    for key in range(0,26):
        encrypt_cezar(key,ciphertext)

# 1.3.2 Sa se cifreze mesajul "MIRACLE" algoritmul utilizat fiind cifrul lui Cezar , cheia de cifrare k=3

# encrypt_cezar(3,"MIRACLE")

# R: "PLUDFOH"

# Exercit¸iul 1.3.3 S˘a se cifreze mesajul:
# CALCULATOR
# algoritmul utilizat fiind cifrul lui Cezar, cheia de cifrare k = 11.

# encrypt_cezar(11,"CALCULATOR")

# R: key: 11 NLWNFWLEZC
