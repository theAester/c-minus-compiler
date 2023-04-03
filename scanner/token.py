from scanner.read import reader
from typing import TextIO

class token:
    tid = -1
    name = "token"

    def check(char: str, lookahead: str = None) -> bool:
        pass

    def capture(char: str) -> (bool, str, str):
        pass

class whitespace(token):
    tid = 0
    name  = "WHITESPACE"

    def check(char:str) -> bool:
        return char in ['\t', '\n', ' ', '\r', '\v', '\f']

    def capture(char:str) -> (bool, str, str):
        string = ''
        while char != None:
            if(whitespace.check(char) == True):
                string = string + char
            else:
                break
            char = reader.next_char()
        return (False, string, char)

class symbol(token):
    tid = 1
    name = "SYMBOL"

    syms = [';',':','[','(','{',']',')','}','+','-','*','=','<','/','==']

    def check(char: str, lookahead: str = None) -> bool:
        if lookahead == None:
            return char in symbol.syms
        else:
            return (char + lookahead) in symbol.syms

    # TODO: legacy code, fix this later
    def capture(char:str):
        string = ''
        while True:
            if(char == '='):
                lookahead = reader.next_char()
                if(lookahead == None or not symbol.check(char, lookahead)):
                    return (False, '=', lookahead)
                else:
                    char = reader.next_char()
                    return (False, '==', char)
            else:
                if(symbol.check(char)):
                    string = string + char
                    char = reader.next_char()
                    return (False, string, char)

class number(token):
    tid = 2
    name = "NUMBER"

    def check(char: str) -> bool:
        return char.isnumeric()

    def capture(char: str) -> (bool, str, str):
        string = ''
        while char != None:
            if number.check(char):
                string  = string + char
                char = reader.next_char()
            else:
                break

        return (False, string, char)

class text(token):
    tid = -2
    name = "text"

    def check(char: str) -> bool:
        return char.isalpha()

    def capture(char: str) -> (bool, str, str):
        string = ''
        while char != None:
            if text.check(char) or number.check(char):
                string = string + char
                char = reader.next_char()
            else:
                break

        return (False, string, char)

class keyword(token):
    tid = 3
    name = "KEYWORD"

    keywords = ['if', 'else', 'void', 'int', 'repeat', 'break', 'until', 'return']

    def check(string:str) -> bool:
        return string in keyword.keywords

    def capture(char: str) -> (bool, str, str):
        pass
