import read as rd
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
        return char in ['\t', '\n', '\u32', '\r', '\v', '\f']

    def capture(char:str) -> (bool, str, str):
        string = ''
        while True:
            if(whitespace.check(char, nextchar) == True):
                string = string + char
            else:
                break
            nextchar = reader.next_char()
            if(nextchar == None):
                return (True, string, None)
        return (False, string, nextchar)

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
            if(char == '=')
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

    def capture(char: str):
        string = ''
        while char != None:
            if number.check(char):
                string  = string + char
                char = reader.next_char()
            else:
                break

        return (False, string, char)
