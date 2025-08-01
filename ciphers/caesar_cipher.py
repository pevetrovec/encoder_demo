from .base_cipher import BaseCipher


class CaesarCipher(BaseCipher):
    name = "caesar"
    parameters = {"shift": 3}

    def encode(self, text: str, shift: int = 3, **kwargs) -> str:
        result = ""
        for char in text:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            else:
                result += char
        return result

    def decode(self, text: str, shift: int = 3, **kwargs) -> str:
        return self.encode(text, -shift)
