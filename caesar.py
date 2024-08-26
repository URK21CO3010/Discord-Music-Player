def caesar_encrypt(plaintext: str, key: int) -> str:
    encrypted_text = []
    
    for char in plaintext:
        if char.isalpha():
            shift = key % 26
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(start + (ord(char) - start + shift) % 26)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)

def caesar_decrypt(ciphertext: str, key: int) -> str:
    decrypted_text = []
    
    for char in ciphertext:
        if char.isalpha():
            shift = key % 26
            start = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr(start + (ord(char) - start - shift) % 26)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)
