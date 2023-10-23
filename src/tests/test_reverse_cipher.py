from ..ciphers.reverse_cipher import reverse_cipher


def test_reverse_cipher_true():
    phrase_to_cipher = "this is a true test"
    result = reverse_cipher(text_input=phrase_to_cipher)
    assert result == "tset eurt a si siht"


def test_reverse_cipher_false():
    phrase_to_cipher = "this is a true test"
    result = reverse_cipher(text_input=phrase_to_cipher)
    assert result != "this is a true test"
    
