from utils.read.readFile import read_plaintext
from utils.helpers.convert import convert_to_ascii
from utils.helpers.convert import ascii_to_hex
from aes.helpers import create_initial_state_with_hex_values
from aes.helpers import create_initial_state_with_ascii_values
from utils.read.readFile import read_subkeys
from aes.helpers import hex_to_ascii_matrix
from aes.helpers import add_round_key

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

state_after_add_round_key = add_round_key(
    initial_state_in_ascii_values, subkey_0_matrix_in_ascii_values
)
print("state_after_add_round_key\n", state_after_add_round_key)

# Part 3 - SubBytes
