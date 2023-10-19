from ..ciphers.caesar_cipher import caesar_cipher


def test_caesar_cipher_true():
    test_phrase = "This is A cipher test that works !"

    result = caesar_cipher(test_phrase, 50, True)

    assert result == "CQRbtRbtytLRYQNatcNbctcQJctfXaTbtu"


def test_caesar_cipher_false():
    test_phrase = "This test is A fail !"

    result = caesar_cipher(test_phrase, 50, True)

    assert result != "This test is A fail !"


def test_caesar_decipher_true():
    test_phrase = "CQRbtRbtytLRYQNatcNbctcQJctfXaTbtu"

    result = caesar_cipher(test_phrase, 50, False)

    assert result == "This is A cipher test that works !"


def test_caesar_decipher_false():
    test_phrase = "CQRbtRbtytLRYQNatcNbctcQJctfXaTbtu"

    result = caesar_cipher(test_phrase, 50, False)

    assert result != "CQRbtRbtytLRYQNatcNbctcQJctfXaTbtu"


def test_caesar_cipher_out_of_boundaries():
    test_phrase = "-_---_--"

    result = caesar_cipher(test_phrase, 0, True)

    assert test_phrase == "-_---_--"


def test_caesar_cipher_out_of_boundaries():
    test_phrase = "-_---_--"

    result = caesar_cipher(test_phrase, 67, False)

    assert test_phrase == "-_---_--"