from aes.helpers import hex_to_ascii_matrix
from aes.helpers import ascii_matrix_to_hex
from aes.helpers import transpose
from aes.helpers import ascii_matrix_to_hex_for_list


def rotate_word(word):
    """
    Rotate a word left by one byte.
    """
    return word[1:] + word[:1]


def substitute_word(word):
    """
    Substitute each byte in a word using the S-box.
    """
    s_box = (
        0x63,
        0x7C,
        0x77,
        0x7B,
        0xF2,
        0x6B,
        0x6F,
        0xC5,
        0x30,
        0x01,
        0x67,
        0x2B,
        0xFE,
        0xD7,
        0xAB,
        0x76,
        0xCA,
        0x82,
        0xC9,
        0x7D,
        0xFA,
        0x59,
        0x47,
        0xF0,
        0xAD,
        0xD4,
        0xA2,
        0xAF,
        0x9C,
        0xA4,
        0x72,
        0xC0,
        0xB7,
        0xFD,
        0x93,
        0x26,
        0x36,
        0x3F,
        0xF7,
        0xCC,
        0x34,
        0xA5,
        0xE5,
        0xF1,
        0x71,
        0xD8,
        0x31,
        0x15,
        0x04,
        0xC7,
        0x23,
        0xC3,
        0x18,
        0x96,
        0x05,
        0x9A,
        0x07,
        0x12,
        0x80,
        0xE2,
        0xEB,
        0x27,
        0xB2,
        0x75,
        0x09,
        0x83,
        0x2C,
        0x1A,
        0x1B,
        0x6E,
        0x5A,
        0xA0,
        0x52,
        0x3B,
        0xD6,
        0xB3,
        0x29,
        0xE3,
        0x2F,
        0x84,
        0x53,
        0xD1,
        0x00,
        0xED,
        0x20,
        0xFC,
        0xB1,
        0x5B,
        0x6A,
        0xCB,
        0xBE,
        0x39,
        0x4A,
        0x4C,
        0x58,
        0xCF,
        0xD0,
        0xEF,
        0xAA,
        0xFB,
        0x43,
        0x4D,
        0x33,
        0x85,
        0x45,
        0xF9,
        0x02,
        0x7F,
        0x50,
        0x3C,
        0x9F,
        0xA8,
        0x51,
        0xA3,
        0x40,
        0x8F,
        0x92,
        0x9D,
        0x38,
        0xF5,
        0xBC,
        0xB6,
        0xDA,
        0x21,
        0x10,
        0xFF,
        0xF3,
        0xD2,
        0xCD,
        0x0C,
        0x13,
        0xEC,
        0x5F,
        0x97,
        0x44,
        0x17,
        0xC4,
        0xA7,
        0x7E,
        0x3D,
        0x64,
        0x5D,
        0x19,
        0x73,
        0x60,
        0x81,
        0x4F,
        0xDC,
        0x22,
        0x2A,
        0x90,
        0x88,
        0x46,
        0xEE,
        0xB8,
        0x14,
        0xDE,
        0x5E,
        0x0B,
        0xDB,
        0xE0,
        0x32,
        0x3A,
        0x0A,
        0x49,
        0x06,
        0x24,
        0x5C,
        0xC2,
        0xD3,
        0xAC,
        0x62,
        0x91,
        0x95,
        0xE4,
        0x79,
        0xE7,
        0xC8,
        0x37,
        0x6D,
        0x8D,
        0xD5,
        0x4E,
        0xA9,
        0x6C,
        0x56,
        0xF4,
        0xEA,
        0x65,
        0x7A,
        0xAE,
        0x08,
        0xBA,
        0x78,
        0x25,
        0x2E,
        0x1C,
        0xA6,
        0xB4,
        0xC6,
        0xE8,
        0xDD,
        0x74,
        0x1F,
        0x4B,
        0xBD,
        0x8B,
        0x8A,
        0x70,
        0x3E,
        0xB5,
        0x66,
        0x48,
        0x03,
        0xF6,
        0x0E,
        0x61,
        0x35,
        0x57,
        0xB9,
        0x86,
        0xC1,
        0x1D,
        0x9E,
        0xE1,
        0xF8,
        0x98,
        0x11,
        0x69,
        0xD9,
        0x8E,
        0x94,
        0x9B,
        0x1E,
        0x87,
        0xE9,
        0xCE,
        0x55,
        0x28,
        0xDF,
        0x8C,
        0xA1,
        0x89,
        0x0D,
        0xBF,
        0xE6,
        0x42,
        0x68,
        0x41,
        0x99,
        0x2D,
        0x0F,
        0xB0,
        0x54,
        0xBB,
        0x16,
    )

    return [s_box[byte] for byte in word]


def generate_next_subkey(subkey):
    """
    Generate the next subkey using the current subkey and round constant.
    """
    # Split the subkey into 4 bytes
    subkey_0_matrix_in_ascii_values = transpose(hex_to_ascii_matrix(subkey))
    # subkey_0_matrix_in_hex_values = transpose(
    #     ascii_matrix_to_hex(subkey_0_matrix_in_ascii_values)
    # )

    # Rotate the last column of the subkey
    rotated_word = rotate_word(subkey_0_matrix_in_ascii_values[3])

    # Substitute the rotated word
    substituted_word = substitute_word(rotated_word)

    # Perform XOR operation after SubBytes
    result_from_subbytes = xor_after_subbytes(substituted_word)

    w0 = subkey_0_matrix_in_ascii_values[0]
    w1 = subkey_0_matrix_in_ascii_values[1]
    w2 = subkey_0_matrix_in_ascii_values[2]
    w3 = subkey_0_matrix_in_ascii_values[3]

    w4 = xor_general(w0, result_from_subbytes)
    w5 = xor_general(w4, w1)
    w6 = xor_general(w5, w2)
    w7 = xor_general(w6, w3)

    return [w4, w5, w6, w7]


def key_expansion(key):
    """
    Perform key expansion to generate round keys from the initial key.
    """
    # Initialize variables
    round_constants = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]
    num_rounds = 10
    subkeys = [key]

    # Generate additional subkeys
    for i in range(1, num_rounds + 1):
        subkey = subkeys[-1]
        round_constant = round_constants[i - 1]

        # Generate the next subkey
        next_subkey = generate_next_subkey(subkey, round_constant)

        # Append the next subkey to the list of subkeys
        subkeys.append(next_subkey)

    return subkeys


def read_subkey(file_path):
    """
    Read the first subkey from the file.
    """
    with open(file_path, "r") as file:
        subkey = (
            file.readline().strip()
        )  # Assuming subkey is stored as a single line in the file
    return subkey


def write_subkey_to_file(subkey, file_path):
    """
    Write the subkey to a file in hexadecimal format.
    """
    with open(file_path, "w") as file:
        file.write(subkey)


def xor_after_subbytes(result_from_subbytes, round_constant=["01", "00", "00", "00"]):
    """
    Perform XOR operation after SubBytes.
    """
    new_result = []
    for i in range(4):
        new_result.append(
            int(hex(result_from_subbytes[i]), base=16) ^ int(round_constant[i], base=16)
        )

    return new_result


def xor_general(list_one, list_two):
    """
    Perform general XOR between 2 lists.
    """
    new_result = []
    for i in range(4):
        new_result.append(
            int(hex(list_one[i]), base=16) ^ int(hex(list_two[i]), base=16)
        )

    return new_result


def main():
    # Read the first subkey from file
    subkey_file_path = "data/subkey_example.txt"
    subkey = read_subkey(subkey_file_path)

    # Generate next subkey
    next_subkey = generate_next_subkey(subkey)

    # ascii version of next key
    next_subkey_hex_version = ascii_matrix_to_hex(next_subkey)

    # Print the next subkey in hexadecimal
    output_string = " ".join(["".join(row) for row in next_subkey_hex_version])
    print("Next subkey in hexadecimal:\n", output_string)

    # Write the result to a file
    result_file_path = "data/result_subkey.txt"
    write_subkey_to_file(output_string, result_file_path)


if __name__ == "__main__":
    main()
