from abc import ABC, abstractmethod


class BaseCipher(ABC):
    """Abstract Base Class for all ciphers."""

    name: str  # Display name of the cipher
    parameters: dict = {}  # Extra parameters (for CLI)

    @abstractmethod
    def encode(self, text: str, **kwargs) -> str:
        pass

    @abstractmethod
    def decode(self, text: str, **kwargs) -> str:
        pass
