from utils.helpers.convert import convert_to_ascii
from aes.helpers import create_initial_state_with_ascii_values
from utils.files.readWrite import read_subkeys
from aes.helpers import hex_to_ascii_matrix
from aes.helpers import add_round_key
from aes.subBytes import sub_bytes
from aes.shiftRows import shift_rows
from aes.helpers import ascii_matrix_to_hex
from aes.mixColumns import mix_columns
from utils.files.readWrite import pad_plaintext
import argparse


def aes_encrypt_block(plaintext_block):
    """
    Encrypt a single block of plaintext message using AES encryption algorithm.
    """
    # Convert block to ASCII values
    block_ascii_values = convert_to_ascii(plaintext_block)

    # Create initial state with ASCII values
    initial_state = create_initial_state_with_ascii_values(block_ascii_values)

    # Add round key
    subkeys_file_path = "data/subkey_example.txt"
    subkeys = read_subkeys(subkeys_file_path)
    subkey_0_hex_string = subkeys[0]
    subkey_0_matrix_in_ascii_values = hex_to_ascii_matrix(subkey_0_hex_string)

    state = add_round_key(initial_state, subkey_0_matrix_in_ascii_values)

    # Perform AES encryption rounds
    # SubBytes
    state = sub_bytes(initial_state)

    # ShiftRows
    state = shift_rows(state)

    # MixColumns
    state = mix_columns(state)

    # Another add round key
    subkey_1_hex_string = subkeys[1]
    subkey_1_matrix_in_ascii_values = hex_to_ascii_matrix(subkey_1_hex_string)
    state = add_round_key(state, subkey_1_matrix_in_ascii_values)

    # Convert the final state to hexadecimal
    state_hex_values = ascii_matrix_to_hex(state)

    return state_hex_values


def aes_encrypt(plaintext):
    """
    Encrypt a plaintext message using AES encryption algorithm.
    """
    # Pad the plaintext if its length is not a multiple of the block size
    padded_plaintext = pad_plaintext(plaintext)

    # Split the padded plaintext into blocks of size 16 bytes (128 bits)
    blocks = [padded_plaintext[i : i + 16] for i in range(0, len(padded_plaintext), 16)]

    # Encrypt each block using AES encryption algorithm
    ciphertext_blocks = []
    for block in blocks:
        # Encrypt a single block
        ciphertext_block = aes_encrypt_block(block)

        # Flatten the list of hexadecimal values into a single string
        flattened_ciphertext_block = "".join(flatten_extend(ciphertext_block))

        # Append the ciphertext block to the list
        ciphertext_blocks.append(flattened_ciphertext_block)

    # Concatenate the ciphertext blocks to get the final ciphertext
    ciphertext = "".join(ciphertext_blocks)

    return ciphertext


def flatten_extend(matrix):
    flat_list = []
    for row in matrix:
        flat_list.extend(row)
    return flat_list


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="AES Encryption Utility")

    # Add argument for plaintext input
    parser.add_argument("plaintext", type=str, help="Input plaintext message")

    #  Parse command-line arguments
    args = parser.parse_args()

    # Perform AES encryption
    ciphertext = aes_encrypt(args.plaintext)

    # Print the ciphertext
    print("Ciphertext:", ciphertext)


if __name__ == "__main__":
    main()
