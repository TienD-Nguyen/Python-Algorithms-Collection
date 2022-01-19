import string

alphabet = string.ascii_lowercase
alphabet_length = len(alphabet)
letter_to_index = dict(zip(alphabet, range(alphabet_length)))
index_to_letter = dict(zip(range(alphabet_length), alphabet))


# Encrypting function of Vigenere Cipher
def encrypt(original_message, key):
    """
    A function that take in English message as input message and encrypt it based on given key word.
    :param original_message: English message that is need to be encrypted
    :param key: A key word that is used to encrypt the message
    :return: Encrypted message.
    """
    encrypted_message = ""
    split_message = [original_message[i:i + len(key)] for i in range(0, len(original_message), len(key))]
    for each_split in split_message:
        i = 0
        for letter in each_split:
            index = (letter_to_index[letter] + letter_to_index[key[i]]) % alphabet_length
            encrypted_message += index_to_letter[index]
            i += 1
    return encrypted_message


# Decrypting function of Vigenere Cipher
def decrypt(cipher_message, key):
    """
    Decrypting a cipher message as an input based on a given key word.
    :param cipher_message: A message that is need to be decrypted
    :param key: A key word to be based on when decrypting messages
    :return: Decrypted message.
    """
    decrypted_message = ""
    split_message = [cipher_message[i:i + len(key)] for i in range(0, len(cipher_message), len(key))]
    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % alphabet_length
            decrypted_message += index_to_letter[number]
            i += 1
    return decrypted_message


# Merge both process into one single function
def vigenere_cipher(cipher_type, input_message, key):
    """
    A function to encrypt or decrypt input messages from the user based on provided key word.
    :param cipher_type: Cipher type that the user want to use ("encrypt" or "decrypt).
    :param input_message: A message that user want to encrypt or a cipher message to be decrypted
    :param key: A key word to be based on when encrypting or decrypting messages
    :return: Return edited messages from encryption or decryption
    """
    edited_message = ""
    key_length = len(key)
    for ind in range(len(input_message)):
        letter_index = letter_to_index[input_message[ind]]
        key_index = letter_to_index[key[ind % key_length]]
        if cipher_type == "decrypt":
            key_index *= -1
        edited_message += index_to_letter[(letter_index + key_index) % alphabet_length]
    return edited_message


def main():
    message = "iaminevitable"
    cipher = vigenere_cipher("encrypt", message, key="hello")
    original = vigenere_cipher("decrypt", cipher, key="hello")ß
    print(cipher)
    print(original)



main()
