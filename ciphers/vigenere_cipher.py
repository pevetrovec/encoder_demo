from .base_cipher import BaseCipher


class VigenereCipher(BaseCipher):
    name = "vigenere"
    parameters = {"key": "KEY"}

    def _shift_char(self, char: str, shift: int) -> str:
        if char.isupper():
            return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        return char

    def encode(self, text: str, key: str = "KEY", **kwargs) -> str:
        result = []
        key = key.lower()
        key_index = 0
        for char in text:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('a')
                result.append(self._shift_char(char, shift))
                key_index += 1
            else:
                result.append(char)
        return ''.join(result)

    def decode(self, text: str, key: str = "KEY", **kwargs) -> str:
        result = []
        key = key.lower()
        key_index = 0
        for char in text:
            if char.isalpha():
                shift = -(ord(key[key_index % len(key)]) - ord('a'))
                result.append(self._shift_char(char, shift))
                key_index += 1
            else:
                result.append(char)
        return ''.join(result)