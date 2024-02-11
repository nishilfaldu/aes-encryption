def read_plaintext(file_path):
    """
    Read plaintext from a file and return it as a string.
    """
    with open(file_path, "r") as file:
        plaintext = file.read()
    return plaintext
