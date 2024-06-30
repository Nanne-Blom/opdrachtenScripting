def encrypt(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + 5
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - 5
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                decrypted_text += chr(shifted)
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

if __name__ == "__main__":
    input_text = input("Geef de tekst die wilt encrypten: ")
    encrypted = encrypt(input_text)
    print(f"Encrypted text: {encrypted}")
    decrypted = decrypt(encrypted)
    print(f"Decrypted text: {decrypted}")
