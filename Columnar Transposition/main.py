def set_permutation_order(key):
    """Creates a permutation order dictionary from the key."""
    key_map = {}
    for i, char in enumerate(key):
        key_map[char] = i
    return key_map

def encrypt_message(msg, key):
    """Encrypts the message using the columnar transposition cipher."""
    key_map = set_permutation_order(key)
    col = len(key)
    row = len(msg) // col + (1 if len(msg) % col else 0)
    matrix = [["_" for _ in range(col)] for _ in range(row)]

    k = 0
    for i in range(row):
        for j in range(col):
            if msg[k] == '\0':  # Handle potential null characters
                matrix[i][j] = '_'
            elif msg[k].isalnum() or msg[k] == ' ':
                matrix[i][j] = msg[k]
            k += 1

    cipher = ""
    for j in sorted(key_map.values()):
        for i in range(row):
            cipher += matrix[i][j]
    return cipher

def decrypt_message(cipher, key):
    """Decrypts the ciphertext using the columnar transposition cipher."""
    col = len(key)
    row = len(cipher) // col
    cipher_matrix = [["_" for _ in range(col)] for _ in range(row)]

    k = 0
    for j in range(col):
        for i in range(row):
            cipher_matrix[i][j] = cipher[k]
            k += 1

    key_map = set_permutation_order(key)
    key_map = {v: k for k, v in key_map.items()}  # Reverse permutation order

    dec_cipher = [["_" for _ in range(col)] for _ in range(row)]

    k = 0
    for j in key_map:
        for i in range(row):
            dec_cipher[i][k] = cipher_matrix[i][j]
        k += 1

    msg = ""
    for i in range(row):
        for j in range(col):
            if dec_cipher[i][j] != '_':
                msg += dec_cipher[i][j]
    return msg

# Driver Program
key = "CODING"
msg = "LIFE OF DEVELOEPRS"

cipher = encrypt_message(msg, key)
print("Encrypted Message:", cipher)

decrypted_msg = decrypt_message(cipher, key)
print("Decrypted Message:", decrypted_msg)
