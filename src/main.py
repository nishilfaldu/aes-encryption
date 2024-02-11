from utils.read.readMessage import read_plaintext
from utils.helpers.convert import convert_to_ascii
from utils.helpers.convert import ascii_to_hex
from aes.helpers import create_initial_state_with_hex_values
from aes.helpers import create_initial_state_with_ascii_values


plaintext_file_path = "data/plaintext.txt"
print("plaintext_file_path:\n", plaintext_file_path)

plaintext = read_plaintext(plaintext_file_path)
print("plaintext:\n", plaintext)

# padded_plaintext = pad_plaintext(plaintext)
ascii_values = convert_to_ascii(plaintext)
print("ascii_values:\n", ascii_values)

hex_values = ascii_to_hex(ascii_values)
print("hex_values:\n", hex_values)

initial_state_in_hex_values = create_initial_state_with_hex_values(hex_values)
print("initial_state_in_hex_values:\n", initial_state_in_hex_values)

initial_state_in_ascii_values = create_initial_state_with_ascii_values(ascii_values)
print("initial_state_in_ascii_values:\n", initial_state_in_ascii_values)
