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
    Convert a hexadecimal string to a transposed 2D matrix of bytes.
    """
    matrix = []
    for i in range(0, 8, 2):  # 8 characters represent 1 column
        column = [int(hex_string[j : j + 2], 16) for j in range(i, len(hex_string), 8)]
        matrix.append(column)
    return matrix


def transpose(matrix):
    """
    Transpose a 2D matrix.
    """
    # Get the number of rows and columns in the original matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Create a new matrix to store the transposed values
    transposed_matrix = [[0] * num_rows for _ in range(num_cols)]

    # Iterate through the original matrix and fill the transposed matrix
    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


def ascii_matrix_to_hex(matrix):
    """
    Convert a 4x4 matrix of ASCII integer values to a 4x4 matrix of hexadecimal strings.
    """
    hex_matrix = []
    for row in matrix:
        hex_row = ["{:02x}".format(byte) for byte in row]
        hex_matrix.append(hex_row)
    return hex_matrix


def ascii_matrix_to_hex_for_list(ascii_list):
    """
    Convert a list of ASCII integer values to a 4x4 matrix of hexadecimal strings.
    """
    hex_list = ["{:02x}".format(byte) for byte in ascii_list]
    return hex_list


def add_round_key(state, subkey):
    """
    Perform AddRoundKey operation on the state using the subkey.
    """
    for i in range(4):
        for j in range(4):
            state[i][j] ^= subkey[i][j]
    return state
