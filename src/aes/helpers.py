def creat_ascii_values_array(ascii_values):
    """
    Divide the plaintext into 16-byte blocks to obtain the initial state.
    """
    initial_state = []
    for i in range(0, len(ascii_values), 16):
        block = ascii_values[i : i + 16]
        initial_state.append(block)
    return initial_state


def create_initial_state_with_hex_values(hex_values):
    """
    Format hexadecimal values into a 2D array with columns of 4, transposed.
    """
    num_rows = len(hex_values) // 4
    hex_matrix = [hex_values[i : i + 4] for i in range(0, len(hex_values), 4)]
    transposed_hex_matrix = [[row[i] for row in hex_matrix] for i in range(4)]
    return transposed_hex_matrix


def create_initial_state_with_ascii_values(ascii_values):
    """
    Format hexadecimal values into a 2D matrix with columns of 4, transposed.
    """
    num_rows = len(ascii_values) // 4
    hex_matrix = [ascii_values[i : i + 4] for i in range(0, len(ascii_values), 4)]
    transposed_hex_matrix = [[row[i] for row in hex_matrix] for i in range(4)]
    return transposed_hex_matrix
