def read_plaintext(file_path):
    """
    Read plaintext from a file and return it as a string.
    """
    with open(file_path, "r") as file:
        plaintext = file.read()
    return plaintext


def read_subkeys(file_path):
    """
    Read subkeys from a file and return them as a list.
    """
    with open(file_path, "r") as file:
        subkeys = file.read().splitlines()
    return subkeys
