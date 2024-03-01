def prepare_text(text):
    text = text.replace(" ", "").upper()
    text = text.replace("J", "I")
    # Add an 'X' between consecutive identical letters
    text = [text[i] if text[i] != text[i + 1] else text[i] + "X" for i in range(len(text) - 1)]
    text.append(text[-1] + "X" if len(text) % 2 != 0 else text[-1])
    return "".join(text)
def generate_key_matrix(key):
    key = key.replace(" ", "").upper()
    key = key.replace("J", "I")
    key_matrix = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in key:
        if char not in key_matrix and char in alphabet:
            key_matrix.append(char)
    for char in alphabet:
        if char not in key_matrix:
            key_matrix.append(char)
    return [key_matrix[i:i+5] for i in range(0, 25, 5)]
def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
def encrypt(plaintext, key):
    plaintext = prepare_text(plaintext)
    key_matrix = generate_key_matrix(key)
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        char1 = plaintext[i]
        char2 = plaintext[i+1]
        row1, col1 = find_position(key_matrix, char1)
        row2, col2 = find_position(key_matrix, char2)
        if row1 == row2:
            ciphertext += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += key_matrix[row1][col2] + key_matrix[row2][col1]
    return ciphertext
def decrypt(ciphertext, key):
    key_matrix = generate_key_matrix(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i+1]
        row1, col1 = find_position(key_matrix, char1)
        row2, col2 = find_position(key_matrix, char2)
        if row1 == row2:
            plaintext += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += key_matrix[row1][col2] + key_matrix[row2][col1]
    return plaintext
# Example usage:
plaintext = "HELLO WORLD!"
key = "KEYWORD"
encrypted_text = encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)
decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
