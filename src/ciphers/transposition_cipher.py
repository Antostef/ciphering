import math

from .utils import type_assert, inbound_assert

@type_assert(str, int)
@inbound_assert(params = {"key": (0, None)})
def transposition_cipher(text_input: str, key: int) -> str:
    """the columnar transposition cipher.

    Args:
        text_input (str): phrase to cipher
        key (int): key to encode

    Returns:
        str: ciphered phrase.
    """
    boxes = [""] * key

    for box in range(key):
        idx = box

        while idx < len(text_input):
            boxes[box] += text_input[idx]

            idx += key

    result = "".join(boxes)  + "|"
    return result


@type_assert(str, int)
@inbound_assert(params = {"key": (0, None)})
def transposition_decipher(text_input: str, key: int) -> str:
    """Columnar transposition decipher.

    Args:
        text_input (str): phrase to decipher
        key (int): key to decode

    Returns:
        str: deciphered phrase.
    """
    text_input = text_input[:-1]
    il = len(text_input)

    box_size = math.ceil(il / key)
    reste = il % key
    result = ""

    for i in range(box_size):
        idx = i 
        while idx < len(text_input):
            result += text_input[idx]
            if idx >= reste * box_size and reste != 0:
                if i == box_size - 1:
                    result = result[:-1]
                    break
                idx += box_size - 1
            else:
                idx += box_size
    return result

