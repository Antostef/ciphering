from .utils import type_assert

@type_assert(str)
def reverse_cipher(text_input: str) -> str:
    """Reverse Cipher is a cipher that returns a reversed version of the string that was given.
    The simplicity of this cipher means that it can be called to cipher and to decipher any message.
    
    Args:
        input_string (str): string that is to be ciphered using the reverse cipher

    Returns:
        str: string using the reverse cipher
    """
    input_reversed = text_input[::-1]
    
    return input_reversed
