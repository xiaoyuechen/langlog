# Generated from xml.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("L\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\b\7\b.\n\b\f\b\16\b\61\13\b\3\t\3\t\3\n")
        buf.write("\5\n\66\n\n\3\n\3\n\3\n\5\n;\n\n\3\13\6\13>\n\13\r\13")
        buf.write("\16\13?\3\f\3\f\3\r\3\r\3\16\6\16G\n\16\r\16\16\16H\3")
        buf.write("\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\2\23")
        buf.write("\n\25\2\27\2\31\13\33\f\3\2\6\4\2C\\c|\3\2\62;\4\2--/")
        buf.write("/\5\2\13\f\17\17\"\"\2N\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2")
        buf.write("\5\37\3\2\2\2\7!\3\2\2\2\t$\3\2\2\2\13&\3\2\2\2\r(\3\2")
        buf.write("\2\2\17*\3\2\2\2\21\62\3\2\2\2\23\65\3\2\2\2\25=\3\2\2")
        buf.write("\2\27A\3\2\2\2\31C\3\2\2\2\33F\3\2\2\2\35\36\7>\2\2\36")
        buf.write("\4\3\2\2\2\37 \7@\2\2 \6\3\2\2\2!\"\7>\2\2\"#\7\61\2\2")
        buf.write("#\b\3\2\2\2$%\7?\2\2%\n\3\2\2\2&\'\7$\2\2\'\f\3\2\2\2")
        buf.write("()\7#\2\2)\16\3\2\2\2*/\5\21\t\2+.\5\21\t\2,.\5\27\f\2")
        buf.write("-+\3\2\2\2-,\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2")
        buf.write("\60\20\3\2\2\2\61/\3\2\2\2\62\63\t\2\2\2\63\22\3\2\2\2")
        buf.write("\64\66\5\31\r\2\65\64\3\2\2\2\65\66\3\2\2\2\66\67\3\2")
        buf.write("\2\2\67:\5\25\13\289\7\60\2\29;\5\25\13\2:8\3\2\2\2:;")
        buf.write("\3\2\2\2;\24\3\2\2\2<>\5\27\f\2=<\3\2\2\2>?\3\2\2\2?=")
        buf.write("\3\2\2\2?@\3\2\2\2@\26\3\2\2\2AB\t\3\2\2B\30\3\2\2\2C")
        buf.write("D\t\4\2\2D\32\3\2\2\2EG\t\5\2\2FE\3\2\2\2GH\3\2\2\2HF")
        buf.write("\3\2\2\2HI\3\2\2\2IJ\3\2\2\2JK\b\16\2\2K\34\3\2\2\2\t")
        buf.write("\2-/\65:?H\3\b\2\2")
        return buf.getvalue()


class xmlLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    STR = 7
    NUM = 8
    SIGN = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<'", "'>'", "'</'", "'='", "'\"'", "'!'" ]

    symbolicNames = [ "<INVALID>",
            "STR", "NUM", "SIGN", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "STR", 
                  "CHAR", "NUM", "DIGITS", "DIGIT", "SIGN", "WS" ]

    grammarFileName = "xml.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


