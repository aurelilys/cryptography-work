from abc import ABC, abstractmethod


class Cipher(ABC):
    @abstractmethod
    def decrypt(self, buffer) -> str:
        pass
