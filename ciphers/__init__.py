import os
import importlib
import inspect
from .base_cipher import BaseCipher

CIPHERS = {}


def load_ciphers():
    """Dynamically load all cipher classes from modules."""
    package_dir = os.path.dirname(__file__)

    for file in os.listdir(package_dir):
        if file.endswith(".py") and file not in ("__init__.py", "base_cipher.py"):
            module_name = f"{__package__}.{file[:-3]}"
            module = importlib.import_module(module_name)

            # Find classes inheriting from BaseCipher
            for _, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, BaseCipher) and obj is not BaseCipher:
                    cipher_instance = obj()
                    CIPHERS[cipher_instance.name] = cipher_instance


load_ciphers()
