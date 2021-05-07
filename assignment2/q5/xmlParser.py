# Generated from xml.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("P\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\2\5\2\27\n\2\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\5\4\37\n\4\3\4\3\4\5\4#\n\4\5\4%\n\4\3\5\3")
        buf.write("\5\3\5\7\5*\n\5\f\5\16\5-\13\5\3\5\7\5\60\n\5\f\5\16\5")
        buf.write("\63\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\5\bD\n\b\3\t\3\t\3\t\7\tI\n\t\f\t\16\t")
        buf.write("L\13\t\3\t\3\t\3\t\2\2\n\2\4\6\b\n\f\16\20\2\2\2P\2\26")
        buf.write("\3\2\2\2\4\30\3\2\2\2\6$\3\2\2\2\b&\3\2\2\2\n\66\3\2\2")
        buf.write("\2\f:\3\2\2\2\16C\3\2\2\2\20E\3\2\2\2\22\23\5\4\3\2\23")
        buf.write("\24\5\2\2\2\24\27\3\2\2\2\25\27\3\2\2\2\26\22\3\2\2\2")
        buf.write("\26\25\3\2\2\2\27\3\3\2\2\2\30\31\5\b\5\2\31\32\5\6\4")
        buf.write("\2\32\33\5\n\6\2\33\5\3\2\2\2\34\36\5\4\3\2\35\37\5\6")
        buf.write("\4\2\36\35\3\2\2\2\36\37\3\2\2\2\37%\3\2\2\2 \"\5\16\b")
        buf.write("\2!#\5\6\4\2\"!\3\2\2\2\"#\3\2\2\2#%\3\2\2\2$\34\3\2\2")
        buf.write("\2$ \3\2\2\2%\7\3\2\2\2&\'\7\3\2\2\'+\7\t\2\2(*\7\f\2")
        buf.write("\2)(\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,\61\3\2\2\2")
        buf.write("-+\3\2\2\2.\60\5\f\7\2/.\3\2\2\2\60\63\3\2\2\2\61/\3\2")
        buf.write("\2\2\61\62\3\2\2\2\62\64\3\2\2\2\63\61\3\2\2\2\64\65\7")
        buf.write("\4\2\2\65\t\3\2\2\2\66\67\7\5\2\2\678\7\t\2\289\7\4\2")
        buf.write("\29\13\3\2\2\2:;\7\t\2\2;<\7\6\2\2<=\7\7\2\2=>\5\16\b")
        buf.write("\2>?\7\7\2\2?\r\3\2\2\2@D\7\n\2\2AD\7\t\2\2BD\5\20\t\2")
        buf.write("C@\3\2\2\2CA\3\2\2\2CB\3\2\2\2D\17\3\2\2\2EF\7\b\2\2F")
        buf.write("J\7\13\2\2GI\7\f\2\2HG\3\2\2\2IL\3\2\2\2JH\3\2\2\2JK\3")
        buf.write("\2\2\2KM\3\2\2\2LJ\3\2\2\2MN\7\t\2\2N\21\3\2\2\2\n\26")
        buf.write("\36\"$+\61CJ")
        return buf.getvalue()


class xmlParser ( Parser ):

    grammarFileName = "xml.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<'", "'>'", "'</'", "'='", "'\"'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "STR", "NUM", 
                      "SIGN", "WS" ]

    RULE_s = 0
    RULE_element = 1
    RULE_content = 2
    RULE_tagstart = 3
    RULE_tagend = 4
    RULE_attrib = 5
    RULE_pod = 6
    RULE_macro = 7

    ruleNames =  [ "s", "element", "content", "tagstart", "tagend", "attrib", 
                   "pod", "macro" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    STR=7
    NUM=8
    SIGN=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(xmlParser.ElementContext,0)


        def s(self):
            return self.getTypedRuleContext(xmlParser.SContext,0)


        def getRuleIndex(self):
            return xmlParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = xmlParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.element()
                self.state = 17
                self.s()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tagstart(self):
            return self.getTypedRuleContext(xmlParser.TagstartContext,0)


        def content(self):
            return self.getTypedRuleContext(xmlParser.ContentContext,0)


        def tagend(self):
            return self.getTypedRuleContext(xmlParser.TagendContext,0)


        def getRuleIndex(self):
            return xmlParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = xmlParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.tagstart()
            self.state = 23
            self.content()
            self.state = 24
            self.tagend()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(xmlParser.ElementContext,0)


        def content(self):
            return self.getTypedRuleContext(xmlParser.ContentContext,0)


        def pod(self):
            return self.getTypedRuleContext(xmlParser.PodContext,0)


        def getRuleIndex(self):
            return xmlParser.RULE_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContent" ):
                listener.enterContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContent" ):
                listener.exitContent(self)




    def content(self):

        localctx = xmlParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [xmlParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.element()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << xmlParser.T__0) | (1 << xmlParser.T__5) | (1 << xmlParser.STR) | (1 << xmlParser.NUM))) != 0):
                    self.state = 27
                    self.content()


                pass
            elif token in [xmlParser.T__5, xmlParser.STR, xmlParser.NUM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.pod()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << xmlParser.T__0) | (1 << xmlParser.T__5) | (1 << xmlParser.STR) | (1 << xmlParser.NUM))) != 0):
                    self.state = 31
                    self.content()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagstartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(xmlParser.STR, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(xmlParser.WS)
            else:
                return self.getToken(xmlParser.WS, i)

        def attrib(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(xmlParser.AttribContext)
            else:
                return self.getTypedRuleContext(xmlParser.AttribContext,i)


        def getRuleIndex(self):
            return xmlParser.RULE_tagstart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTagstart" ):
                listener.enterTagstart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTagstart" ):
                listener.exitTagstart(self)




    def tagstart(self):

        localctx = xmlParser.TagstartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tagstart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(xmlParser.T__0)
            self.state = 37
            self.match(xmlParser.STR)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==xmlParser.WS:
                self.state = 38
                self.match(xmlParser.WS)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==xmlParser.STR:
                self.state = 44
                self.attrib()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(xmlParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagendContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(xmlParser.STR, 0)

        def getRuleIndex(self):
            return xmlParser.RULE_tagend

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTagend" ):
                listener.enterTagend(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTagend" ):
                listener.exitTagend(self)




    def tagend(self):

        localctx = xmlParser.TagendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tagend)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(xmlParser.T__2)
            self.state = 53
            self.match(xmlParser.STR)
            self.state = 54
            self.match(xmlParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttribContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(xmlParser.STR, 0)

        def pod(self):
            return self.getTypedRuleContext(xmlParser.PodContext,0)


        def getRuleIndex(self):
            return xmlParser.RULE_attrib

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttrib" ):
                listener.enterAttrib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttrib" ):
                listener.exitAttrib(self)




    def attrib(self):

        localctx = xmlParser.AttribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(xmlParser.STR)
            self.state = 57
            self.match(xmlParser.T__3)
            self.state = 58
            self.match(xmlParser.T__4)
            self.state = 59
            self.pod()
            self.state = 60
            self.match(xmlParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(xmlParser.NUM, 0)

        def STR(self):
            return self.getToken(xmlParser.STR, 0)

        def macro(self):
            return self.getTypedRuleContext(xmlParser.MacroContext,0)


        def getRuleIndex(self):
            return xmlParser.RULE_pod

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPod" ):
                listener.enterPod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPod" ):
                listener.exitPod(self)




    def pod(self):

        localctx = xmlParser.PodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_pod)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [xmlParser.NUM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(xmlParser.NUM)
                pass
            elif token in [xmlParser.STR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.match(xmlParser.STR)
                pass
            elif token in [xmlParser.T__5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.macro()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MacroContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIGN(self):
            return self.getToken(xmlParser.SIGN, 0)

        def STR(self):
            return self.getToken(xmlParser.STR, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(xmlParser.WS)
            else:
                return self.getToken(xmlParser.WS, i)

        def getRuleIndex(self):
            return xmlParser.RULE_macro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro" ):
                listener.enterMacro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro" ):
                listener.exitMacro(self)




    def macro(self):

        localctx = xmlParser.MacroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_macro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(xmlParser.T__5)
            self.state = 68
            self.match(xmlParser.SIGN)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==xmlParser.WS:
                self.state = 69
                self.match(xmlParser.WS)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self.match(xmlParser.STR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





