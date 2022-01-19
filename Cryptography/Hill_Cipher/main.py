import string
import numpy as np
from egcd import egcd

alphabet = string.ascii_lowercase + " !?"
alphabet_length = len(alphabet)
letter_to_index = dict(zip(alphabet, range(alphabet_length)))
index_to_letter = dict(zip(range(alphabet_length), alphabet))


def generate_matrix_key(keywords):
    """
    This function generates a matrix of N x N size based on keywords given by the user as input.
    :param keywords: A string keywords inputted by the user that would be used for encrypting and decrypting.
    :return: Return a matrix key with the size of N * N that serve the purpose of encrypting and decrypting messages.
    """
    n = int(np.sqrt(len(keywords)))
    matrix_key = [letter_to_index[character] for character in keywords]
    matrix_key = np.asarray(matrix_key).reshape(n, n)
    return matrix_key


def inverse_modulus_matrix(matrix, modulus):
    """
    This function generates inverse modulus matrix that would be used to decrypt messages based on generated matrix.
    :param matrix: The matrix that is used to encrypt message
    :param modulus: For modulo operation, which would be the length of the alphabet in this case.
    :return: Return the inverse matrix against the modulus to decrypt the message.
    """
    det = int(np.round(np.linalg.det(matrix)))
    inv_matrix = np.linalg.inv(matrix)
    inv_det = egcd(det, modulus)[1] % modulus
    inverse_modulus_matrix = (inv_det * np.round(det * inv_matrix).astype(int) % modulus)
    return inverse_modulus_matrix


def encrypt(message, K):
    """
    This function encrypts the input message from the user with the use of K (the key matrix of size n x n)
    :param message: The input message from the user that would need to be encrypted
    :param K: The matrix of size n-by-n that is used to encrypting message
    :return: Return the encrypted message.
    """
    encrypted = ""
    message_in_numbers = []

    for letter in message:
        message_in_numbers.append(letter_to_index[letter])

    split_P = [message_in_numbers[i:i + int(K.shape[0])] for i in range(0, len(message_in_numbers), int(K.shape[0]))]

    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]

        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter_to_index[" "])[:, np.newaxis]

        cipher_numbers = np.dot(K, P) % alphabet_length
        rows_number = cipher_numbers.shape[0]

        for row in range(rows_number):
            number = int(cipher_numbers[row, 0])
            encrypted += index_to_letter[number]

    return encrypted


def decrypt(cipher, K_inv):
    """
    This function decrypts the input cipher message from the user with the use of K^-1 (an inverse key matrix of size n x n)
    :param cipher: A cipher message that is need to be decrypted
    :param K_inv: An inverse matrix against modulus
    :return: Return the decrypted message.
    """
    decrypted = ""
    cipher_in_numbers = []

    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])

    split_C = [cipher_in_numbers[i:i + int(K_inv.shape[0])] for i in range(0, len(cipher_in_numbers), int(K_inv.shape[0]))]

    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]

        numbers = np.dot(K_inv, C) % alphabet_length
        rows_numbers = numbers.shape[0]

        for row in range(rows_numbers):
            number = int(numbers[row, 0])
            decrypted += index_to_letter[number]

    return decrypted


def main():
    message = "i am iron man"
    key = "qweasdzxc"

    K = generate_matrix_key(key)
    K_inv = inverse_modulus_matrix(K, alphabet_length)

    cipher_message = encrypt(message, K)
    decrypted_message = decrypt(cipher_message, K_inv)

    print(cipher_message)
    print(decrypted_message)


main()
