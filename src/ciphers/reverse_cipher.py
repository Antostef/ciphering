def reverse_cipher(input_string: str) -> str:
    """Reverse Cipher is a cipher that returns a reversed version of the string that was given.
    The simplicity of this cipher means that it can be called to cipher and to decipher any message.
    
    Args:
        input_string (str): string that is to be ciphered using the reverse cipher

    Returns:
        str: string using the reverse cipher
    """
    input_reversed = input_string[::-1]
    
    return input_reversed
