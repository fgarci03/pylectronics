from typing import Tuple


def decimal_to_boolean_list(num: int, padding: int = 0) -> Tuple[bool, ...]:
    """
    Convert a decimal number into a tuple of booleans, representing its binary value.
    """
    # Convert the decimal into binary
    binary = bin(num).replace('0b', '').zfill(padding)

    # Return a tuple of booleans, one for each element of the binary number (it's either '0' or '1' so we can convert
    # directly to boolean)
    return tuple(char == '1' for char in binary)
