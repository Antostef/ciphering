from ..ciphers.transposition_cipher import transposition_cipher, transposition_decipher

def test_transposition_cipher_true():
    text = "this is a test message"
    key = 8

    result = transposition_cipher(text, key)

    assert result == "taeh sitssea sgites  m|"


def test_transposition_cipher_false(): 
    text = "this is a test message"
    key = 8

    result = transposition_decipher(text, key)

    assert result != "this is a test message"


def test_transposition_decipher_true():
    text = "taeh sitssea sgites  m|"
    key = 8

    result = transposition_decipher(text, key)

    assert result == "this is a test message"


def test_transposition_decipher_false():
    text = "taeh sitssea sgites  m|"
    key = 8

    result = transposition_decipher(text, key)

    assert result != "taeh sitssea sgites  m|"