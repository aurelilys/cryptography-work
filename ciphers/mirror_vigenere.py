from ciphers.vigenere import Vigenere


class MirrorVigenere(Vigenere):
    initial_key = ""
    shift = []

    def __init__(self, key, shift):
        super().__init__(key)
        self.initial_key = key
        self.shift = shift

    def decrypt(self, buffer) -> str:
        result = ""
        lines = buffer.splitlines()

        for index, value in enumerate(lines):
            line = value[::-1]
            line_shift = self.shift[index]

            self.key = self.initial_key[line_shift::] + self.initial_key[0:line_shift]
            result += super().decrypt(line) + '\n'

        return result
