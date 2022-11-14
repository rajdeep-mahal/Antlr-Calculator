# Generated from Expr.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,13,67,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,
        1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,
        1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,4,10,55,8,10,11,10,12,10,
        56,1,11,4,11,60,8,11,11,11,12,11,61,1,12,1,12,1,12,1,12,0,0,13,1,
        1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,1,
        0,3,2,0,10,10,13,13,1,0,48,57,3,0,9,10,13,13,32,32,68,0,1,1,0,0,
        0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,
        13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,
        23,1,0,0,0,0,25,1,0,0,0,1,27,1,0,0,0,3,29,1,0,0,0,5,31,1,0,0,0,7,
        35,1,0,0,0,9,39,1,0,0,0,11,43,1,0,0,0,13,45,1,0,0,0,15,47,1,0,0,
        0,17,49,1,0,0,0,19,51,1,0,0,0,21,54,1,0,0,0,23,59,1,0,0,0,25,63,
        1,0,0,0,27,28,5,40,0,0,28,2,1,0,0,0,29,30,5,41,0,0,30,4,1,0,0,0,
        31,32,5,115,0,0,32,33,5,105,0,0,33,34,5,110,0,0,34,6,1,0,0,0,35,
        36,5,99,0,0,36,37,5,111,0,0,37,38,5,115,0,0,38,8,1,0,0,0,39,40,5,
        116,0,0,40,41,5,97,0,0,41,42,5,110,0,0,42,10,1,0,0,0,43,44,5,94,
        0,0,44,12,1,0,0,0,45,46,5,43,0,0,46,14,1,0,0,0,47,48,5,45,0,0,48,
        16,1,0,0,0,49,50,5,42,0,0,50,18,1,0,0,0,51,52,5,47,0,0,52,20,1,0,
        0,0,53,55,7,0,0,0,54,53,1,0,0,0,55,56,1,0,0,0,56,54,1,0,0,0,56,57,
        1,0,0,0,57,22,1,0,0,0,58,60,7,1,0,0,59,58,1,0,0,0,60,61,1,0,0,0,
        61,59,1,0,0,0,61,62,1,0,0,0,62,24,1,0,0,0,63,64,7,2,0,0,64,65,1,
        0,0,0,65,66,6,12,0,0,66,26,1,0,0,0,3,0,56,61,1,0,1,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    TRIG_SIN = 3
    TRIG_COS = 4
    TRIG_TAN = 5
    OP_POW = 6
    OP_ADD = 7
    OP_SUB = 8
    OP_MUL = 9
    OP_DIV = 10
    NEWLINE = 11
    INT = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'sin'", "'cos'", "'tan'", "'^'", "'+'", "'-'", 
            "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "TRIG_SIN", "TRIG_COS", "TRIG_TAN", "OP_POW", "OP_ADD", "OP_SUB", 
            "OP_MUL", "OP_DIV", "NEWLINE", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "TRIG_SIN", "TRIG_COS", "TRIG_TAN", "OP_POW", 
                  "OP_ADD", "OP_SUB", "OP_MUL", "OP_DIV", "NEWLINE", "INT", 
                  "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


