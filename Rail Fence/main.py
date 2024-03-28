def encrypt_rail_fence(text, key):
    encrypted_text = ''
    rail = [[' ' for _ in range(len(text))] for _ in range(key)]
    
    # Fill the rail matrix
    row = 0
    down = False
    for i in range(len(text)):
        if row == 0 or row == key - 1:
            down = not down
        rail[row][i] = text[i]
        row = row + 1 if down else row - 1
    
    # Read encrypted text from rail matrix
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != ' ':
                encrypted_text += rail[i][j]

    return encrypted_text

def decrypt_rail_fence(text, key):
    decrypted_text = ''
    rail = [[' ' for _ in range(len(text))] for _ in range(key)]
    
    # Fill the rail matrix with '*' characters indicating positions to be filled
    row = 0
    down = False
    for i in range(len(text)):
        if row == 0 or row == key - 1:
            down = not down
        rail[row][i] = '*'
        row = row + 1 if down else row - 1
    
    # Fill the '*' positions with characters from the encrypted text
    index = 0
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] == '*' and index < len(text):
                rail[i][j] = text[index]
                index += 1
    
    # Read decrypted text from rail matrix
    row = 0
    down = False
    for i in range(len(text)):
        if row == 0 or row == key - 1:
            down = not down
        decrypted_text += rail[row][i]
        row = row + 1 if down else row - 1

    return decrypted_text

def main():
    text = input("Enter the text: ")
    key = int(input("Enter the key: "))
    choice = input("Encrypt (1) or Decrypt (2): ")

    if choice == '1':
        print("Encrypted Text:", encrypt_rail_fence(text, key))
    elif choice == '2':
        print("Decrypted Text:", decrypt_rail_fence(text, key))
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
