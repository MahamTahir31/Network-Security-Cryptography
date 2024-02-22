def create_vigenere_matrix():
    mat = [['' for _ in range(26)] for _ in range(26)]

    for i in range(26):
        for j in range(26):
            mat[i][j] = chr((i + j) % 26 + ord('A'))
    return mat
def find_intersection(plaintext, keyword):
    plaintext_index = ord(plaintext) - ord('A')
    keyword_index = ord(keyword) - ord('A')
    vigenere_matrix = create_vigenere_matrix()
    intersection = vigenere_matrix[keyword_index][plaintext_index]
    return intersection
def vigenere_encrypt(plaintext):
    encrypted_text = []
    fixed_key = "LOCK"
    vigenere_matrix = create_vigenere_matrix()
    print("Vigenere Cipher Matrix:")
    for row in vigenere_matrix:
        print(" ".join(row))
    print("\nEncryption Process:")
    print("--------------------------------------------------------")
    print("| Plain Text | Key Char | Intersection | Encrypted Char |")
    print("--------------------------------------------------------")
    for i in range(len(plaintext)):
        plaintext_char = plaintext[i]
        keyword_char = fixed_key[i % len(fixed_key)]
        intersection = find_intersection(plaintext_char, keyword_char)
        encrypted_text.append(intersection)

        print("|     {}     |    {}     |      {}       |        {}        |".format(
            plaintext_char, keyword_char, intersection, intersection))
    print("--------------------------------------------------------")
    return ''.join(encrypted_text)
def vigenere_decrypt(encrypted_text):
    decrypted_text = []
    fixed_key = "LOCK"
    vigenere_matrix = create_vigenere_matrix()
    print("Vigenere Cipher Matrix:")
    for row in vigenere_matrix:
        print(" ".join(row))
    print("\nDecryption Process:")
    print("--------------------------------------------------------")
    print("| Encrypted Char | Key Char | Intersection | Plain Text |")
    print("--------------------------------------------------------")
    for i in range(len(encrypted_text)):
        encrypted_char = encrypted_text[i]
        keyword_char = fixed_key[i % len(fixed_key)]
        keyword_index = ord(keyword_char) - ord('A')
        encrypted_index = -1
        for j in range(26):
            if vigenere_matrix[keyword_index][j] == encrypted_char:
                encrypted_index = j
                break
        if encrypted_index != -1:
            decrypted_char = chr(encrypted_index + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append('?')

        print("|     {}     |    {}     |      {}       |      {}     |".format(
            encrypted_char, keyword_char, encrypted_char, decrypted_text[i]))
    print("--------------------------------------------------------")
    return ''.join(decrypted_text)
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))
if __name__ == "__main__":
    option = input("Choose option:\n1. Encryption (Enter 'E')\n2. Decryption (Enter 'D')\n").upper()
    if option == 'E':
        plaintext = input("Enter the plaintext: ").upper()
        encrypted_text = vigenere_encrypt(plaintext)
        print("Encrypted Text:", encrypted_text)
    elif option == 'D':
        encrypted_text = input("Enter the encrypted text: ").upper()
        decrypted_text = vigenere_decrypt(encrypted_text)
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid option!")
