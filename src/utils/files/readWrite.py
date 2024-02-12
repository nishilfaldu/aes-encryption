def read_plaintext(file_path):
    """
    Read plaintext from a file and return it as a string.
    """
    with open(file_path, "r") as file:
        plaintext = file.read()

    padded_plain_text = pad_plaintext(plaintext)
    return padded_plain_text


def read_subkeys(file_path):
    """
    Read subkeys from a file and return them as a list.
    """
    with open(file_path, "r") as file:
        subkeys = file.read().splitlines()
    return subkeys


def write_to_file(file_path, data):
    """
    Write data to a file.
    """
    with open(file_path, "w") as file:
        for item in data:
            if isinstance(item, list):
                if len(item) > 0 and isinstance(
                    item[0], list
                ):  # Check if item is a 2D list (like a matrix)
                    for row in item:
                        file.write(
                            " ".join(map(str, row)) + "\n"
                        )  # Write each row to a new line
                    file.write("\n")  # Add a newline between matrices
                else:  # If it's a 1D list (like a single row of a matrix)
                    file.write(
                        " ".join(map(str, item)) + "\n"
                    )  # Write the single row to a new line
                    file.write("\n")  # Add a newline after writing the single row
            else:
                file.write(str(item) + "\n")  # Write other data types to file

    print(f"\n\n\nData written to {file_path}\n\n\n")


def pad_plaintext(plaintext):
    """
    Pad the plaintext to make its length a multiple of the block size.
    """
    block_size = 16  # AES block size is 128 bits (16 bytes)
    padding_length = block_size - (len(plaintext) % block_size)

    # If the plaintext length is already a multiple of the block size, no padding is needed
    if padding_length == 16:
        return plaintext

    # Convert padding bytes to characters for better readability
    padding = chr(padding_length) * padding_length
    return plaintext + padding
