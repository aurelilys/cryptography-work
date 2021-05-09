import string

from ciphers.lib import Cipher


class Vigenere(Cipher):
    key = ""

    def __init__(self, key):
        self.key = key

    def decrypt(self, buffer: str) -> str:
        result = ""
        position = 0

        for character in buffer:
            print(character)
            if character not in string.ascii_lowercase:
                result += character
            else:
                index = string.ascii_lowercase.index(character)
                index_key = string.ascii_lowercase.index(self.key[position])

                result += string.ascii_lowercase[abs((index - index_key) % 26)]

            position += 1
            if position == len(self.key):
                position = 0
        return result
