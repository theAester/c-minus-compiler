import read as rd
from typing import TextIO

class token:
    tid = -1
    name = "token"

    def check(char: str, lookahead: str = None) -> bool:
        pass

    def capture(char: str, infile: TextIO) -> (bool, str, str):
        pass

class whitespace(token):
    tid = 0
    name  = "whitespace"

    def check(char:str) -> bool:
        return char in ['\t', '\n', '\u32', '\r', '\v', '\f']

    def capture(char:str, infile:TextIO) -> (bool, str, str):
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
    name = "symbol"

    syms = [';',':','[','(','{',']',')','}','+','-','*','=','<','/','==']

    def check(char: str, lookahead: str = None) -> bool:
        if lookahead == None:
            return char in symbol.syms
        else:
            return (char + lookahead) in symbol.syms

    def capture(char:str, infile:TextIO):
        string = ''
        while True:
            if(char == '=')
                lookahead = reader.next_char()
                if(lookahead == None or not symbol.check(char, lookahead)):
                    return (True, '=', lookahead)
                else:
                    char = reader.next_char()
                    return (False, '==', char)
            else:
                if(symbol.check())

