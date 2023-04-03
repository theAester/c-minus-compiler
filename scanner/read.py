class reader:
    infile = None
    def init(filename):
        reader.infile = open(filename, 'r')

    def next_char():
        char = reader.infile.read(1)
        if char == '':
            return None
        return char
