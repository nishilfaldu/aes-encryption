def shift_rows(state):
    """
    Shift rows of the state matrix.
    """
    # Shift second row one position to the left
    state[1] = state[1][1:] + state[1][:1]

    # Shift third row two positions to the left
    state[2] = state[2][2:] + state[2][:2]

    # Shift fourth row three positions to the left
    state[3] = state[3][3:] + state[3][:3]

    return state
