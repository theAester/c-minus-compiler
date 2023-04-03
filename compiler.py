import scannr
import scanner.token as tk
from scanner.read import reader


if __name__ == "__main__":
    reader.init("input.txt")

    tokens = scannr.get_next_token()

    for token in tokens:
        print('({}, {}, {})'.format(token[0], token[1], token[2]))
