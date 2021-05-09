import sys

from ciphers.alphabet_substitution import AlphabetSubstitution
from ciphers.mirror_vigenere import MirrorVigenere
from ciphers.vigenere import Vigenere


def main(arguments):
    if len(arguments) != 2:
        print("Usage: main.py <input> <method>")
        return

    buffer = read_file(arguments[0])
    cipher = generate_cipher(arguments[1])

    if cipher is None:
        print("Invalid method. Available: as-one (text 1), as-two (text 2)")
        return

    print("Result:", cipher.decrypt(buffer))


def read_file(name):
    with open('samples\\' + name, 'r', encoding='utf-8') as file:
        output = file.read()
    return output


def generate_cipher(method):
    switcher = {
        "as-one": AlphabetSubstitution(
            ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z', 'a']),
        "as-two": AlphabetSubstitution(
            ['y', 'w', 'd', 'n', 'q', 'm', 'l', 'x', 's', 'j', 'i', 'h', 'g', 'a', 'r', ' ', 'p', ' ', 'o', 'k', 't',
             'c', 'f', 'e', 'u', 'z']),
        "vg-three": Vigenere("clez"),
        "vg-four": MirrorVigenere("bravez", [1, 0, 0, 2, 4, 5, 0, 3, 4, 5, 0, 4, 5, 0, 4, 5, 1, 5, 0])
    }

    return switcher.get(method, None)


if __name__ == '__main__':
    main(sys.argv[1:])
