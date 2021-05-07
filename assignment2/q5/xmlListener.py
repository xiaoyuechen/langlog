# Generated from xml.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .xmlParser import xmlParser
else:
    from xmlParser import xmlParser


# This class defines a complete listener for a parse tree produced by xmlParser.
class xmlListener(ParseTreeListener):
    def __init__(self):
        self.element_as_attrib = False
        self.has_children = False
        self.podtable = {}

    # Enter a parse tree produced by xmlParser#s.
    def enterS(self, ctx: xmlParser.SContext):
        pass

    # Exit a parse tree produced by xmlParser#s.
    def exitS(self, ctx: xmlParser.SContext):
        pass

    # Enter a parse tree produced by xmlParser#element.
    def enterElement(self, ctx: xmlParser.ElementContext):
        self.element_as_attrib = len(
            ctx.tagstart().attrib()) == 0 and ctx.content().element() == None
        self.has_children = ctx.content().element() != None

        if not self.has_children:
            name = ctx.tagstart().STR().getText()
            if name not in self.podtable:
                self.podtable[name] = []
            num = ctx.content().pod().NUM()
            if num is not None:
                num = int(num.getText())
                self.podtable[name].append(num)

    # Exit a parse tree produced by xmlParser#element.
    def exitElement(self, ctx: xmlParser.ElementContext):
        pass

    # Enter a parse tree produced by xmlParser#content.
    def enterContent(self, ctx: xmlParser.ContentContext):
        pass

    # Exit a parse tree produced by xmlParser#content.
    def exitContent(self, ctx: xmlParser.ContentContext):
        pass

    # Enter a parse tree produced by xmlParser#tagstart.
    def enterTagstart(self, ctx: xmlParser.TagstartContext):
        print(f"\"{ctx.STR()}\": ", end='')
        if not self.element_as_attrib:
            print(f"{{")

    # Exit a parse tree produced by xmlParser#tagstart.
    def exitTagstart(self, ctx: xmlParser.TagstartContext):
        if not self.element_as_attrib and not self.has_children:
            print("\"POD\": ", end='')

    # Enter a parse tree produced by xmlParser#tagend.
    def enterTagend(self, ctx: xmlParser.TagendContext):
        if not self.element_as_attrib:
            print(f"\n}},")
        else:
            print()

    # Exit a parse tree produced by xmlParser#tagend.
    def exitTagend(self, ctx: xmlParser.TagendContext):
        self.element_as_attrib = False

    # Enter a parse tree produced by xmlParser#attrib.
    def enterAttrib(self, ctx: xmlParser.AttribContext):
        print(f"\"{ctx.STR()}\": ", end='')

    # Exit a parse tree produced by xmlParser#attrib.
    def exitAttrib(self, ctx: xmlParser.AttribContext):
        print()

    # Enter a parse tree produced by xmlParser#pod.
    def enterPod(self, ctx: xmlParser.PodContext):
        if ctx.NUM() is not None:
            print(f"{ctx.NUM()}", end='')
        elif ctx.STR() is not None:
            print(f"\"{ctx.STR()}\"", end='')
        elif ctx.macro() is not None:
            target = ctx.macro().STR().getText()
            op = ctx.macro().SIGN().getText()
            if op == '+':
                print(sum(self.podtable[target]), end='')
            elif op == '-':
                print(self.podtable[target][0] - self.podtable[target][1],
                      end='')
        print(",", end='')

    # Exit a parse tree produced by xmlParser#pod.
    def exitPod(self, ctx: xmlParser.PodContext):
        pass

    # Enter a parse tree produced by xmlParser#macro.
    def enterMacro(self, ctx: xmlParser.MacroContext):
        pass

    # Exit a parse tree produced by xmlParser#macro.
    def exitMacro(self, ctx: xmlParser.MacroContext):
        pass


del xmlParser
