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
        4,0,15,78,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,2,14,7,14,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,
        1,10,1,11,1,11,1,11,1,11,1,12,4,12,66,8,12,11,12,12,12,67,1,13,4,
        13,71,8,13,11,13,12,13,72,1,14,1,14,1,14,1,14,0,0,15,1,1,3,2,5,3,
        7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,
        1,0,3,2,0,10,10,13,13,1,0,48,57,3,0,9,10,13,13,32,32,79,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,
        0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,
        0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,1,31,1,0,0,0,
        3,33,1,0,0,0,5,35,1,0,0,0,7,39,1,0,0,0,9,43,1,0,0,0,11,47,1,0,0,
        0,13,49,1,0,0,0,15,51,1,0,0,0,17,53,1,0,0,0,19,55,1,0,0,0,21,57,
        1,0,0,0,23,60,1,0,0,0,25,65,1,0,0,0,27,70,1,0,0,0,29,74,1,0,0,0,
        31,32,5,40,0,0,32,2,1,0,0,0,33,34,5,41,0,0,34,4,1,0,0,0,35,36,5,
        115,0,0,36,37,5,105,0,0,37,38,5,110,0,0,38,6,1,0,0,0,39,40,5,99,
        0,0,40,41,5,111,0,0,41,42,5,115,0,0,42,8,1,0,0,0,43,44,5,116,0,0,
        44,45,5,97,0,0,45,46,5,110,0,0,46,10,1,0,0,0,47,48,5,94,0,0,48,12,
        1,0,0,0,49,50,5,43,0,0,50,14,1,0,0,0,51,52,5,45,0,0,52,16,1,0,0,
        0,53,54,5,42,0,0,54,18,1,0,0,0,55,56,5,47,0,0,56,20,1,0,0,0,57,58,
        5,112,0,0,58,59,5,105,0,0,59,22,1,0,0,0,60,61,3,27,13,0,61,62,5,
        46,0,0,62,63,3,27,13,0,63,24,1,0,0,0,64,66,7,0,0,0,65,64,1,0,0,0,
        66,67,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,26,1,0,0,0,69,71,7,
        1,0,0,70,69,1,0,0,0,71,72,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,
        28,1,0,0,0,74,75,7,2,0,0,75,76,1,0,0,0,76,77,6,14,0,0,77,30,1,0,
        0,0,3,0,67,72,1,0,1,0
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
    PI = 11
    DEC = 12
    NEWLINE = 13
    INT = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'sin'", "'cos'", "'tan'", "'^'", "'+'", "'-'", 
            "'*'", "'/'", "'pi'" ]

    symbolicNames = [ "<INVALID>",
            "TRIG_SIN", "TRIG_COS", "TRIG_TAN", "OP_POW", "OP_ADD", "OP_SUB", 
            "OP_MUL", "OP_DIV", "PI", "DEC", "NEWLINE", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "TRIG_SIN", "TRIG_COS", "TRIG_TAN", "OP_POW", 
                  "OP_ADD", "OP_SUB", "OP_MUL", "OP_DIV", "PI", "DEC", "NEWLINE", 
                  "INT", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


