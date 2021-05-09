import string

from ciphers.lib import Cipher


class AlphabetSubstitution(Cipher):
    alphabet = []

    def __init__(self, alphabet):
        self.alphabet = alphabet

    def decrypt(self, buffer) -> str:
        result = ""

        for character in buffer:
            if not character.isalpha():
                result += character
                continue

            index = string.ascii_lowercase.index(character)
            result += self.alphabet[index]
        return result
