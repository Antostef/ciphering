from .utils import type_assert, inbound_assert

@type_assert(str, int, bool)
@inbound_assert(params = {"key": (0, None)})
def caesar_cipher(text_input: str, key: int, mode: bool) -> str:
    """Caesar cipher

    Args:
        text_input (str): text to be ciphered
        key (int): number representing the offset that will encode the text
        mode (str): ciphering (true) or deciphering (false)

    Returns:
        str: _description_
    """
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'"
    result = ""

    for char in text_input:
        idx = symbols.find(char)

        if idx >= 0:
            symbols_array_length = len(symbols)

            if mode:
                offset_idx = idx + (key % symbols_array_length)
                offset_symbol_idx = offset_idx % symbols_array_length
            else:
                offset_idx = idx - (key % symbols_array_length)
                offset_symbol_idx = offset_idx if offset_idx >= 0 else symbols_array_length + offset_idx 
            result += symbols[offset_symbol_idx]
        else:
            result += char
    
    return result
                
