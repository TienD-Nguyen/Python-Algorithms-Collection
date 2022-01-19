# Importing "string" package to access ASCII lower case alphabet characters
import string


alphabet = string.ascii_lowercase
alphabet_length = len(alphabet)
letter_to_index = dict(zip(alphabet, range(alphabet_length)))
index_to_letter = dict(zip(range(alphabet_length), alphabet))


def encrypt(message, shift=3):
    """
    A function that would take in a message as input and shift each letter by defined amount
    to generate encrypted message.
    """
    encrypted_message = ""
    for letter in message:
        index = (letter_to_index[letter] + shift) % alphabet_length
        encrypted_letter = index_to_letter[index]
        encrypted_message += encrypted_letter
    return encrypted_message


def decrypt(cipher_message, shift=3):
    """
    A function that would take in an encrypted message as input and shift each letter by defined
    amount back to original message.
    :param cipher_message: Encrypted messages or words that are needed to decrypt
    :param shift: The amount of letter to be shifted when decrypt messages
    :return:
    """
    decrypted_message = ""
    for letter in cipher_message:
        index = (letter_to_index[letter] - shift) % alphabet_length
        decrypted_letter = index_to_letter[index]
        decrypted_message += decrypted_letter
    return decrypted_message


# Merge both functions into one single function that require cryptography type as an input
def caesar_cipher(cryptography_type, original_message, shift=3):
    """
    The function that decrypt or encrypt messages based on user's specification by shifting each letter
    toward defined amount.
    :param cryptography_type: Specify crytography text "encrypt" or "decrypt"
    :param original_message: The original message that is needed to decrypt or encrypt
    :param shift: The amount of letter to be shifted when encrypt or decrypt messages
    :return:
    """
    if cryptography_type == "decrypt":
        shift *= -1
    edited_message = ""
    for letter in original_message:
        index = (letter_to_index[letter] + shift) % alphabet_length
        shifted_letter = index_to_letter[index]
        edited_message += shifted_letter
    return edited_message



message = "iloveyou"
cipher_message = caesar_cipher("encrypt", message, shift=3)
original_message = caesar_cipher("decrypt", cipher_message, shift=3)
print(cipher_message)
print(original_message)
