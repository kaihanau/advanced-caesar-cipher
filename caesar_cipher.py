# Define a single comprehensive character set
all_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
             ':', ';', '<', '=', '>', '?', '@', '[', '\', ']', '^', '_', '`', '{', '|', '}', '~']

# Get user input for operation type, message, and shift value
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))


# Function to encrypt a message using the simplified Caesar cipher
def encrypt(original_text, shift_amount):
    cipher_text = ""  # Initialize empty string to store the encrypted message
    for char in original_text:  # Loop through each character in the original text
        if char in all_chars:  # Check if character is in our character set
            position = all_chars.index(char)
            shifted_position = (position + shift_amount) % len(all_chars)
            cipher_text += all_chars[shifted_position]
        else:  # For any character not in our set
            cipher_text += char  # Keep it unchanged
    
    print(f"Here is the encoded result: {cipher_text}")  # Display the encrypted message


# Function to decrypt a message using the simplified Caesar cipher
def decrypt(original_text, shift_amount):
    decoded_message = ""  # Initialize empty string to store the decrypted message
    for char in original_text:  # Loop through each character
        if char in all_chars:  # Check if character is in our character set
            position = all_chars.index(char)
            shifted_position = (position - shift_amount) % len(all_chars)
            decoded_message += all_chars[shifted_position]
        else:  # For any character not in our set
            decoded_message += char  # Keep it unchanged

    print(f"Here is the decoded message: {decoded_message}")  # Display the decrypted message


# Combined function that handles both encryption and decryption
def caesar(original_text, shift_amount):
    # Make sure the shift is within a reasonable range
    shift_amount = shift_amount % len(all_chars)
    
    if direction.lower() == "encode":  # If user wants to encrypt
        encrypt(original_text, shift_amount)  # Call the encrypt function
    elif direction.lower() == "decode":  # If user wants to decrypt
        decrypt(original_text, shift_amount)  # Call the decrypt function
    else:
        print("You chose a wrong action. Please type 'encode' or 'decode'.")  # Error message for invalid input

# Call the main caesar function with user inputs
caesar(text, shift)
