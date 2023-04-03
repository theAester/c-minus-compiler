import scanner.token as tk
from scanner.read import reader
#import scanner.panic as pc

def get_next_token():
    char = reader.next_char()
    err = True
    lexeme = ''
    lineno = 1
    while char != None:
        
        # TODO: handle comments

        # check every class of tokens

        if(tk.whitespace.check(char)):
            _, lexeme, char = tk.whitespace.capture(char, infile)
            if lexeme == '\n':
                lineno += 1
            continue

        if(tk.symbols.check(char)):
            err, lexeme, char = tk.symbol.capture(char, infile)
            if err == False:
                yield ('SYMBOL', lexeme, lineno)
            continue
