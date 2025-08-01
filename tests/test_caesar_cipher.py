import json
import pytest
from ciphers.caesar_cipher import CaesarCipher

cipher = CaesarCipher()

# Load test data from JSON file once
with open("tests/data/caesar_test_cases.json") as f:
    test_data = json.load(f)


@pytest.mark.parametrize("plain_text, shift, expected_cipher",
                         [(case["input"], case["shift"], case["expected"]) for case in test_data["encode"]])
def test_encode(plain_text, shift, expected_cipher):
    assert cipher.encode(plain_text, shift=shift) == expected_cipher


@pytest.mark.parametrize("cipher_text, shift, expected_plain",
                         [(case["input"], case["shift"], case["expected"]) for case in test_data["decode"]])
def test_decode(cipher_text, shift, expected_plain):
    assert cipher.decode(cipher_text, shift=shift) == expected_plain