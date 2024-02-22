def char_to_value(ch):
    return ord(ch) - ord('A')
def value_to_char(value):
    return chr(value + ord('A'))
def vigenere_encrypt(plaintext):
    key = "PASCAL"
    encrypted_text = []
    print("Encryption Process:")
    print("-------------------------------------------------------------------")
    print("| Plain Text | Pi Values | Key Stream | Cipher Values | Cipher Text |")
    print("-------------------------------------------------------------------")
    for i in range(len(plaintext)):
        plain_char = plaintext[i]
        key_char = key[i % len(key)]
        plain_value = char_to_value(plain_char)
        key_value = char_to_value(key_char)
        encrypted_value = (plain_value + key_value) % 26
        encrypted_char = value_to_char(encrypted_value)
        encrypted_text.append(encrypted_char)
        print("|     {}     |    {:2d}     |     {}      |      {:2d}       |     {}      |".format(
            plain_char, plain_value, key_char, encrypted_value, encrypted_char))
    print("-------------------------------------------------------------------")
    print("Cipher Text:", ''.join(encrypted_text))
def vigenere_decrypt(encrypted_text):
    key = "PASCAL"
    decrypted_text = []
    print("\nDecryption Process:")
    print("-------------------------------------------------------------------")
    print("| Cipher Text | Cipher Values | Key Stream | Pi Values | Plain Text |")
    print("-------------------------------------------------------------------")
    for i in range(len(encrypted_text)):
        encrypted_char = encrypted_text[i]
        key_char = key[i % len(key)]
        encrypted_value = char_to_value(encrypted_char)
        key_value = char_to_value(key_char)
        decrypted_value = (encrypted_value - key_value + 26) % 26
        decrypted_char = value_to_char(decrypted_value)
        decrypted_text.append(decrypted_char)
        print("|     {}     |      {:2d}       |     {}      |     {:2d}     |     {}     |".format(
            encrypted_char, encrypted_value, key_char, decrypted_value, decrypted_char))
    print("-------------------------------------------------------------------")
    print("Decrypted Text:", ''.join(decrypted_text))
if __name__ == "__main__":
    option = int(input("Choose option:\n1. Encryption\n2. Decryption\n"))
    if option == 1:
        plaintext = input("Enter the plaintext: ").upper()
        vigenere_encrypt(plaintext)
    elif option == 2:
        encrypted_text = input("Enter the encrypted text: ").upper()
        vigenere_decrypt(encrypted_text)
    else:
        print("Invalid option!")
