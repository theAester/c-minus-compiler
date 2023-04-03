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
            _, lexeme, char = tk.whitespace.capture(char)
            if '\n' in lexeme:
                lineno += 1
            continue

        if(tk.symbol.check(char)):
            err, lexeme, char = tk.symbol.capture(char)
            if err == False:
                yield (tk.symbol.name, lexeme, lineno)
            continue

        if(tk.number.check(char)):
            err, lexeme, char = tk.number.capture(char)
            if(err == False):
                yield (tk.number.name, lexeme, lineno)
            continue

        if(tk.text.check(char)):
            err, lexeme, char = tk.text.capture(char)
            if(err == False):
                if(tk.keyword.check(lexeme)):
                    yield (tk.keyword.name, lexeme, lineno)
                else:
                    yield ("ID", lexeme, lineno)
            continue
