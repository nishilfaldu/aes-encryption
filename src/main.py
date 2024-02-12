from utils.files.readWrite import read_plaintext
from utils.helpers.convert import convert_to_ascii
from utils.helpers.convert import ascii_to_hex
from aes.helpers import create_initial_state_with_hex_values
from aes.helpers import create_initial_state_with_ascii_values
from utils.files.readWrite import read_subkeys
from aes.helpers import hex_to_ascii_matrix
from aes.helpers import add_round_key
from aes.subBytes import sub_bytes
from aes.shiftRows import shift_rows
from aes.helpers import ascii_matrix_to_hex
from aes.mixColumns import mix_columns
from utils.files.readWrite import write_to_file


# Part 1
plaintext_file_path = "data/plaintext.txt"
print("plaintext_file_path:\n", plaintext_file_path)

plaintext = read_plaintext(plaintext_file_path)
print("plaintext:\n", plaintext)

ascii_values = convert_to_ascii(plaintext)
print("ascii_values:\n", ascii_values)

hex_values = ascii_to_hex(ascii_values)
print("hex_values:\n", hex_values)

initial_state_in_hex_values = create_initial_state_with_hex_values(hex_values)
print("initial_state_in_hex_values:\n", initial_state_in_hex_values)

initial_state_in_ascii_values = create_initial_state_with_ascii_values(ascii_values)
print("initial_state_in_ascii_values:\n", initial_state_in_ascii_values)

# Part 2 - calculate one AddKey before Round 1 with subkey0
subkeys_file_path = "data/subkey_example.txt"
print("\nsubkeys_file_path:\n", subkeys_file_path)

subkeys = read_subkeys(subkeys_file_path)
print("subkeys:\n", subkeys)

subkey_0_hex_string = subkeys[0]
print("subkey_0:\n", subkey_0_hex_string)

subkey_0_matrix_in_ascii_values = hex_to_ascii_matrix(subkey_0_hex_string)
print("subkey_0_matrix:\n", subkey_0_matrix_in_ascii_values)

subkey_0_matrix_in_hex_values = ascii_matrix_to_hex(subkey_0_matrix_in_ascii_values)
print("subkey_0_matrix_in_hex_values:\n", subkey_0_matrix_in_hex_values)

state_in_ascii_after_add_round_key = add_round_key(
    initial_state_in_ascii_values, subkey_0_matrix_in_ascii_values
)
print("state_in_ascii_after_add_round_key\n", state_in_ascii_after_add_round_key)

state_in_hex_after_add_round_key = ascii_matrix_to_hex(
    state_in_ascii_after_add_round_key
)
print("state_in_hex_after_add_round_key:\n", state_in_hex_after_add_round_key)

# Part 3 - SubBytes
state_in_ascii_after_sub_bytes = sub_bytes(state_in_ascii_after_add_round_key)
print("state_in_ascii_after_sub_bytes\n", state_in_ascii_after_sub_bytes)

state_in_hex_after_sub_bytes = ascii_matrix_to_hex(state_in_ascii_after_sub_bytes)
print("state_in_hex_after_sub_bytes:\n", state_in_hex_after_sub_bytes)

# Part 4 - ShiftRows
state_in_ascii_after_shift_rows = shift_rows(state_in_ascii_after_sub_bytes)
print("state_in_ascii_after_shift_rows\n", state_in_ascii_after_shift_rows)

state_in_hex_after_shift_rows = ascii_matrix_to_hex(state_in_ascii_after_shift_rows)
print("state_in_hex_after_shift_rows:\n", state_in_hex_after_shift_rows)

# Part 5 - MixColumns
state_in_ascii_after_mix_columns = mix_columns(state_in_ascii_after_shift_rows)
print("state_in_ascii_after_mix_columns\n", state_in_ascii_after_mix_columns)

state_in_hex_after_mix_columns = ascii_matrix_to_hex(state_in_ascii_after_mix_columns)
print("state_in_hex_after_mix_columns:\n", state_in_hex_after_mix_columns)

# Part 6 - another add_round_key
subkey_1_hex_string = subkeys[1]
print("subkey_1:\n", subkey_1_hex_string)

subkey_1_matrix_in_ascii_values = hex_to_ascii_matrix(subkey_1_hex_string)
print("subkey_1_matrix:\n", subkey_1_matrix_in_ascii_values)

subkey_1_matrix_in_hex_values = ascii_matrix_to_hex(subkey_1_matrix_in_ascii_values)
print("subkey_0_matrix_in_hex_values:\n", subkey_1_matrix_in_hex_values)

state_in_ascii_after_add_round_key_2 = add_round_key(
    state_in_ascii_after_mix_columns, subkey_1_matrix_in_ascii_values
)
print(
    "state_in_ascii_after_add_round_key_2:\n",
    state_in_ascii_after_add_round_key_2,
)

state_in_hex_after_add_round_key_2 = ascii_matrix_to_hex(
    state_in_ascii_after_add_round_key_2
)
print("state_in_hex_after_add_round_key_2:\n", state_in_hex_after_add_round_key_2)


# Part 7 - Add all data printed using the statements above in a file
output_file_path = "data/result.txt"
output_data = [
    "plaintext_file_path:",
    plaintext_file_path,
    "plaintext:",
    plaintext,
    "ascii_values:",
    ascii_values,
    "hex_values:",
    hex_values,
    "initial_state_in_hex_values:",
    initial_state_in_hex_values,
    "initial_state_in_ascii_values:",
    initial_state_in_ascii_values,
    "subkeys_file_path:",
    subkeys_file_path,
    "subkeys:",
    subkeys,
    "subkey_0:",
    subkey_0_hex_string,
    "subkey_0_matrix_in_ascii_values:",
    subkey_0_matrix_in_ascii_values,
    "subkey_0_matrix_in_hex_values:",
    subkey_0_matrix_in_hex_values,
    "state_in_ascii_after_add_round_key:",
    state_in_ascii_after_add_round_key,
    "state_in_hex_after_add_round_key:",
    state_in_hex_after_add_round_key,
    "state_in_ascii_after_sub_bytes:",
    state_in_ascii_after_sub_bytes,
    "state_in_hex_after_sub_bytes:",
    state_in_hex_after_sub_bytes,
    "state_in_ascii_after_shift_rows:",
    state_in_ascii_after_shift_rows,
    "state_in_hex_after_shift_rows:",
    state_in_hex_after_shift_rows,
    "state_in_ascii_after_mix_columns:",
    state_in_ascii_after_mix_columns,
    "state_in_hex_after_mix_columns:",
    state_in_hex_after_mix_columns,
    "subkey_1:",
    subkey_1_hex_string,
    "subkey_1_matrix_in_ascii_values:",
    subkey_1_matrix_in_ascii_values,
    "subkey_1_matrix_in_hex_values:",
    subkey_1_matrix_in_hex_values,
    "state_in_ascii_after_add_round_key_2:",
    state_in_ascii_after_add_round_key_2,
    "state_in_hex_after_add_round_key_2:",
    state_in_hex_after_add_round_key_2,
]

write_to_file(output_file_path, output_data)
