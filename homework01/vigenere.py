def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    key = ""
    if len(keyword) > 0:
        while len(key) < len(plaintext): 
            key += keyword
        a = 0
        for i in plaintext:
            if i.isalpha():
                lcFlag = i.islower()
                if lcFlag:
                    if (ord(i) + ord(key[a]) - ord("a")) <= ord("z"):
                        ciphertext += chr(ord(i) + ord(key[a]) - ord("a"))
                    else:
                        ciphertext += chr(ord(i) + ord(key[a]) - ord("z") - 1)
                else:
                    if (ord(i) + ord(key[a]) - ord("A")) <= ord("Z"):
                        ciphertext += chr(ord(i) + ord(key[a]) - ord("A"))
                    else:
                        ciphertext += chr(ord(i) + ord(key[a]) - ord("Z") - 1)
            else:
                ciphertext += i
            a += 1
    else:
        ciphertext = plaintext

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    key = ""
    if len(keyword) > 0:
        while len(key) < len(ciphertext):
            key += keyword
        a = 0
        for i in ciphertext:
            if i.isalpha():
                lcFlag = i.islower()
                if lcFlag:
                    if ord(i) - (ord(key[a]) - ord("a")) >= ord("a"): 
                        plaintext += chr(ord(i) - ord(key[a]) + ord("a"))
                    else:
                        plaintext += chr(ord(i) - ord(key[a]) + ord("z") + 1)
                else:
                    # ord(i) - keyLen
                    # keylen = ord(key[a]) - ord("A")
                    if ord(i) - (ord(key[a]) - ord("A")) >= ord("A"): 
                        plaintext += chr(ord(i) - ord(key[a]) + ord("A"))
                    else:
                        plaintext += chr(ord(i) - ord(key[a]) + ord("Z") + 1)

            else:
                plaintext += i
            a += 1
    else:
        plaintext = ciphertext
    
    return plaintext


# print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))
# print(decrypt_vigenere("txMmDERKZvPaKerwXnRHMrljyeGMA,gKkqAJnZId NPFpI,rkokzKwTpkbnZfmq", ""))