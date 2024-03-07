class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, plaintext):
        encrypted_text = ""
        for char in plaintext:
            if char.isalpha():
                shifted = ord(char) + self.shift
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    elif shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    elif shifted < ord('A'):
                        shifted += 26
                encrypted_text += chr(shifted)
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, ciphertext):
        decrypted_text = ""
        for char in ciphertext:
            if char.isalpha():
                shifted = ord(char) - self.shift
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    elif shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    elif shifted < ord('A'):
                        shifted += 26
                decrypted_text += chr(shifted)
            else:
                decrypted_text += char
        return decrypted_text