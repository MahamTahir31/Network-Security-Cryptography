morse_code = {
    'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..",
    'e': ".", 'f': "..-.", 'g': "--.", 'h': "....",
    'i': "..", 'j': ".---", 'k': "-.-", 'l': ".--",
    'm': "--", 'n': "-.", 'o': "---", 'p': ".--.",
    'q': "--.-", 'r': ".-.", 's': "...", 't': "-",
    'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-",
    'y': "-.--", 'z': "--..", ' ': " "
}

def display_table_header():
    print("{:<15s} {:<15s}".format("Plain Text", "Pattern"))
    print("---------------------------")

def display_table_entry(letter, pattern):
    print("{:<15s} {:<15s}".format(letter, pattern))

def encrypt(message):
    encrypted_message = ""
    for char in message:
        if char.lower() in morse_code:
            encrypted_message += morse_code[char.lower()] + " "
    return encrypted_message

def decrypt(pattern):
    decrypted_message = ""
    current_pattern = ""
    pattern += " "  # Add a space at the end to ensure the last pattern is processed
    for char in pattern:
        if char == ' ':
            for letter, value in morse_code.items():
                if current_pattern == value:
                    decrypted_message += letter
                    break
            current_pattern = ""
        else:
            current_pattern += char
    return decrypted_message

print("\t\t\t\t\t Welcome to Morse Code Encryption & Decryption program!")

while True:
    print("What do you like to do?")
    print("1-Encrypt a message")
    print("2-Decrypt a message")
    print("3-Exit")
    choice = int(input())

    if choice > 3:
        print("Invalid choice!\nPlease choose another choice")
        continue
    else:
        if choice == 1:
            message = input("Please enter the message you want to encrypt:\n")
            encrypted_message = encrypt(message)

            display_table_header()
            display_table_entry(message, encrypted_message)

        elif choice == 2:
            pattern = input("Please enter the message you want to decipher:\n")
            decrypted_message = decrypt(pattern)

            display_table_header()
            display_table_entry(decrypted_message, pattern)

        elif choice == 3:
            print("Thank you for using Morse Code!")
            break
