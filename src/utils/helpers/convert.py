def convert_to_ascii(plaintext):
    """
    Convert each character in the plaintext to its ASCII representation.
    """
    ascii_values = [ord(char) for char in plaintext]
    return ascii_values


def ascii_to_hex(ascii_values):
    """
    Convert an array of ASCII values to hexadecimal representation.
    """
    hex_array = [hex(value)[2:].zfill(2) for value in ascii_values]
    return hex_array
