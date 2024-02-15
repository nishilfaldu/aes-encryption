import numpy as np


def hex_to_matrix(hex_string):
    """
    Convert a hexadecimal string to a 4x4 matrix of integers.
    """
    matrix = []
    for i in range(0, len(hex_string), 2):
        row = [int(hex_string[i : i + 2], 16) for i in range(0, len(hex_string), 2)]
        matrix.append(row)
    return np.array(matrix)


def mix_columns(state):
    """
    Mix columns of the state matrix using AES MixColumns operation.
    """
    polynomial_matrix = np.array(
        [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]], dtype=np.uint8
    )

    mixed_state = np.zeros_like(state)

    for i in range(4):
        for j in range(4):
            mixed_state[i][j] = (
                gf_mul(polynomial_matrix[i][0], state[0][j])
                ^ gf_mul(polynomial_matrix[i][1], state[1][j])
                ^ gf_mul(polynomial_matrix[i][2], state[2][j])
                ^ gf_mul(polynomial_matrix[i][3], state[3][j])
            )

    return mixed_state.tolist()


def gf_mul(a, b):  # Source: StackOverflow
    """
    Galois Field (GF(2^8)) multiplication of two numbers.
    """
    p = 0b100011011
    m = 0
    for i in range(8):
        m = m << 1
        if m & 0b100000000:
            m = m ^ p
        if b & 0b010000000:
            m = m ^ a
        b = b << 1
    return m
