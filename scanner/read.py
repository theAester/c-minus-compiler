class reader:
    infile = None
    def next_char():
        char = reader.infile.read(1)
        if char == '':
            return None
        return char
