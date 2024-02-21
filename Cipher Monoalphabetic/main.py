def encrypt(text, key_shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) + key_shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + key_shift - 97) % 26 + 97)

    return result

def decrypt(text, key_shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - key_shift - 65 + 26) % 26 + 65)
        else:
            result += chr((ord(char) - key_shift - 97 + 26) % 26 + 97)

    return result

def main():
    text = input("\nEnter the text: ")
    key_shift = int(input("Enter the shift value: "))

    encrypted_text = encrypt(text, key_shift)
    print("\nEncrypted Text:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, key_shift)
    print("\nDecrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
