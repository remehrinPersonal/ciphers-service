def caesar_encode(plain_text, shift):
    cipher_text = ""
    for c in plain_text:
        if c.isalpha():
            if c.islower():
                base = ord('a')
            else:
                base = ord('A')
            c_encoded = ((ord(c) - base + shift) % 26) + base
            c_encoded = chr(c_encoded)
        else:
            c_encoded = c 
        cipher_text += c_encoded
    return cipher_text