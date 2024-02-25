def char_to_value(ch):
    return ord(ch.upper()) - ord('A')

def value_to_char(value):
    return chr(value + ord('A'))

def custom_xor_encrypt(plaintext, key):
    encrypted_text = ""
    for i in range(len(plaintext)):
        plain_char = plaintext[i]
        key_char = key[i % len(key)]
        
        plain_value = char_to_value(plain_char)
        key_value = char_to_value(key_char)
        
        encrypted_value = (plain_value ^ key_value) % 26
        
        encrypted_char = value_to_char(encrypted_value)
        
        encrypted_text += encrypted_char
    return encrypted_text

def custom_xor_decrypt(encrypted_text, key):
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        encrypted_char = encrypted_text[i]
        key_char = key[i % len(key)]
        
        encrypted_value = char_to_value(encrypted_char)
        key_value = char_to_value(key_char)
        
        decrypted_value = (encrypted_value ^ key_value) % 26
        
        decrypted_char = value_to_char(decrypted_value)
        
        decrypted_text += decrypted_char
    return decrypted_text

def main():
    plaintext = input("Enter the plain text: ").upper()
    key = input("Enter the key: ").upper()
    
    if len(key) != len(plaintext):
        print("Error: Key length must be equal to the size of the plain text.")
        return 1
    
    encrypted_text = custom_xor_encrypt(plaintext, key)
    print("Encrypted Text:", encrypted_text)
    
    decrypted_text = custom_xor_decrypt(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
