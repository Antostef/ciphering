from ..ciphers.caesar_cipher import caesar_cipher


def test_caesar_cipher_true():
    test_phrase = "This is A cipher test that works !"

    result = caesar_cipher(text_input=test_phrase, key=50, mode=True)

    assert result == "CQRbtRbtytLRYQNatcNbctcQJctfXaTbtu"


def test_caesar_cipher_false():
    test_phrase = "This test is A fail !"

    result = caesar_cipher(text_input=test_phrase, key=50, mode=True)

    assert result != "This test is A fail !"


def test_caesar_decipher_true():
    test_phrase = "CQRbtRbtytLRYQNatcNbctcQJctfXaTbtu"

    result = caesar_cipher(text_input=test_phrase, key=50, mode=False)

    assert result == "This is A cipher test that works !"


def test_caesar_decipher_false():
    test_phrase = "CQRbtRbtytLRYQNatcNbctcQJctfXaTbtu"

    result = caesar_cipher(text_input=test_phrase, key=50, mode=False)

    assert result != "CQRbtRbtytLRYQNatcNbctcQJctfXaTbtu"


def test_caesar_cipher_out_of_boundaries():
    test_phrase = "-_---_--"

    result = caesar_cipher(text_input=test_phrase, key=0, mode=True)

    assert test_phrase == "-_---_--"


def test_caesar_cipher_out_of_boundaries():
    test_phrase = "-_---_--"

    result = caesar_cipher(text_input=test_phrase, key=67, mode=False)

    assert test_phrase == "-_---_--"