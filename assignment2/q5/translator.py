import sys
from antlr4 import *
from xmlLexer import xmlLexer
from xmlParser import xmlParser
from xmlListener import xmlListener


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = xmlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = xmlParser(stream)
    tree = parser.s()
    listener = xmlListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


if __name__ == '__main__':
    main(sys.argv)
