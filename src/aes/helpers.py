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


def hex_to_ascii_matrix(hex_string):
    """
    Convert a hexadecimal string to a 2D matrix of bytes.
    """
    matrix = []
    for i in range(0, len(hex_string), 8):  # 8 characters represent 1 row
        row = [
            int(hex_string[i : i + 2], 16),
            int(hex_string[i + 2 : i + 4], 16),
            int(hex_string[i + 4 : i + 6], 16),
            int(hex_string[i + 6 : i + 8], 16),
        ]
        matrix.append(row)
    return matrix


def add_round_key(state, subkey):
    """
    Perform AddRoundKey operation on the state using the subkey.
    """
    for i in range(4):
        for j in range(4):
            state[i][j] ^= subkey[i][j]
    return state
