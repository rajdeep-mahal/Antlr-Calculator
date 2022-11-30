# Generated from Expr.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,27,61,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,3,1,34,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,
        45,8,1,10,1,12,1,48,9,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,57,8,3,1,
        4,1,4,1,4,0,1,2,5,0,2,4,6,8,0,4,1,0,19,21,1,0,17,18,1,0,4,7,1,0,
        8,15,66,0,10,1,0,0,0,2,33,1,0,0,0,4,49,1,0,0,0,6,56,1,0,0,0,8,58,
        1,0,0,0,10,11,3,2,1,0,11,12,5,0,0,1,12,1,1,0,0,0,13,14,6,1,-1,0,
        14,15,3,4,2,0,15,16,5,1,0,0,16,17,3,2,1,0,17,18,5,2,0,0,18,34,1,
        0,0,0,19,20,3,8,4,0,20,21,5,1,0,0,21,22,3,2,1,0,22,23,5,2,0,0,23,
        34,1,0,0,0,24,34,3,6,3,0,25,26,5,1,0,0,26,27,3,2,1,0,27,28,5,2,0,
        0,28,34,1,0,0,0,29,30,5,1,0,0,30,31,3,2,1,0,31,32,5,3,0,0,32,34,
        1,0,0,0,33,13,1,0,0,0,33,19,1,0,0,0,33,24,1,0,0,0,33,25,1,0,0,0,
        33,29,1,0,0,0,34,46,1,0,0,0,35,36,10,8,0,0,36,37,5,16,0,0,37,45,
        3,2,1,9,38,39,10,7,0,0,39,40,7,0,0,0,40,45,3,2,1,8,41,42,10,6,0,
        0,42,43,7,1,0,0,43,45,3,2,1,7,44,35,1,0,0,0,44,38,1,0,0,0,44,41,
        1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,3,1,0,0,0,48,
        46,1,0,0,0,49,50,7,2,0,0,50,5,1,0,0,0,51,57,1,0,0,0,52,57,5,26,0,
        0,53,57,5,24,0,0,54,57,5,22,0,0,55,57,5,23,0,0,56,51,1,0,0,0,56,
        52,1,0,0,0,56,53,1,0,0,0,56,54,1,0,0,0,56,55,1,0,0,0,57,7,1,0,0,
        0,58,59,7,3,0,0,59,9,1,0,0,0,4,33,44,46,56
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "')!'", "'log10'", "'sqrt'", 
                     "'cbrt'", "'ln'", "'deg'", "'rad'", "'cosh'", "'sinh'", 
                     "'tanh'", "'sin'", "'cos'", "'tan'", "'^'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'pi'", "'e'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "LOG_BASE_10", "SQRT", "CUBE_RT", "NATURAL_LOG", "TRIG_DEG", 
                      "TRIG_RAD", "TRIG_COSH", "TRIG_SINH", "TRIG_TANH", 
                      "TRIG_SIN", "TRIG_COS", "TRIG_TAN", "OP_POW", "OP_ADD", 
                      "OP_SUB", "OP_MUL", "OP_DIV", "OP_MOD", "PI", "EULER", 
                      "DEC", "NEWLINE", "INT", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_exponential = 2
    RULE_term = 3
    RULE_trig = 4

    ruleNames =  [ "prog", "expr", "exponential", "term", "trig" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    LOG_BASE_10=4
    SQRT=5
    CUBE_RT=6
    NATURAL_LOG=7
    TRIG_DEG=8
    TRIG_RAD=9
    TRIG_COSH=10
    TRIG_SINH=11
    TRIG_TANH=12
    TRIG_SIN=13
    TRIG_COS=14
    TRIG_TAN=15
    OP_POW=16
    OP_ADD=17
    OP_SUB=18
    OP_MUL=19
    OP_DIV=20
    OP_MOD=21
    PI=22
    EULER=23
    DEC=24
    NEWLINE=25
    INT=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.expr(0)
            self.state = 11
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class InfixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def OP_POW(self):
            return self.getToken(ExprParser.OP_POW, 0)
        def OP_MUL(self):
            return self.getToken(ExprParser.OP_MUL, 0)
        def OP_DIV(self):
            return self.getToken(ExprParser.OP_DIV, 0)
        def OP_MOD(self):
            return self.getToken(ExprParser.OP_MOD, 0)
        def OP_SUB(self):
            return self.getToken(ExprParser.OP_SUB, 0)
        def OP_ADD(self):
            return self.getToken(ExprParser.OP_ADD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfixExpr" ):
                listener.enterInfixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfixExpr" ):
                listener.exitInfixExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfixExpr" ):
                return visitor.visitInfixExpr(self)
            else:
                return visitor.visitChildren(self)


    class TermExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ExprParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermExpr" ):
                listener.enterTermExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermExpr" ):
                listener.exitTermExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermExpr" ):
                return visitor.visitTermExpr(self)
            else:
                return visitor.visitChildren(self)


    class TrigExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def trig(self):
            return self.getTypedRuleContext(ExprParser.TrigContext,0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrigExpr" ):
                listener.enterTrigExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrigExpr" ):
                listener.exitTrigExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrigExpr" ):
                return visitor.visitTrigExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensExpr" ):
                listener.enterParensExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensExpr" ):
                listener.exitParensExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)


    class ExponentialExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exponential(self):
            return self.getTypedRuleContext(ExprParser.ExponentialContext,0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponentialExpr" ):
                listener.enterExponentialExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponentialExpr" ):
                listener.exitExponentialExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponentialExpr" ):
                return visitor.visitExponentialExpr(self)
            else:
                return visitor.visitChildren(self)


    class FactorialExpressionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorialExpression" ):
                listener.enterFactorialExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorialExpression" ):
                listener.exitFactorialExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactorialExpression" ):
                return visitor.visitFactorialExpression(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = ExprParser.ExponentialExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 14
                self.exponential()
                self.state = 15
                self.match(ExprParser.T__0)
                self.state = 16
                self.expr(0)
                self.state = 17
                self.match(ExprParser.T__1)
                pass

            elif la_ == 2:
                localctx = ExprParser.TrigExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 19
                self.trig()
                self.state = 20
                self.match(ExprParser.T__0)
                self.state = 21
                self.expr(0)
                self.state = 22
                self.match(ExprParser.T__1)
                pass

            elif la_ == 3:
                localctx = ExprParser.TermExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.term()
                pass

            elif la_ == 4:
                localctx = ExprParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(ExprParser.T__0)
                self.state = 26
                self.expr(0)
                self.state = 27
                self.match(ExprParser.T__1)
                pass

            elif la_ == 5:
                localctx = ExprParser.FactorialExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self.match(ExprParser.T__0)
                self.state = 30
                self.expr(0)
                self.state = 31
                self.match(ExprParser.T__2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 44
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.InfixExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 36
                        localctx.op = self.match(ExprParser.OP_POW)
                        self.state = 37
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.InfixExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 39
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 40
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.InfixExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 42
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 43
                        localctx.right = self.expr(7)
                        pass

             
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExponentialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOG_BASE_10(self):
            return self.getToken(ExprParser.LOG_BASE_10, 0)

        def NATURAL_LOG(self):
            return self.getToken(ExprParser.NATURAL_LOG, 0)

        def SQRT(self):
            return self.getToken(ExprParser.SQRT, 0)

        def CUBE_RT(self):
            return self.getToken(ExprParser.CUBE_RT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_exponential

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponential" ):
                listener.enterExponential(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponential" ):
                listener.exitExponential(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponential" ):
                return visitor.visitExponential(self)
            else:
                return visitor.visitChildren(self)




    def exponential(self):

        localctx = ExprParser.ExponentialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_exponential)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 240) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def DEC(self):
            return self.getToken(ExprParser.DEC, 0)

        def PI(self):
            return self.getToken(ExprParser.PI, 0)

        def EULER(self):
            return self.getToken(ExprParser.EULER, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = ExprParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term)
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(ExprParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.match(ExprParser.DEC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.match(ExprParser.PI)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 55
                self.match(ExprParser.EULER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TrigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRIG_COS(self):
            return self.getToken(ExprParser.TRIG_COS, 0)

        def TRIG_SIN(self):
            return self.getToken(ExprParser.TRIG_SIN, 0)

        def TRIG_TAN(self):
            return self.getToken(ExprParser.TRIG_TAN, 0)

        def TRIG_DEG(self):
            return self.getToken(ExprParser.TRIG_DEG, 0)

        def TRIG_RAD(self):
            return self.getToken(ExprParser.TRIG_RAD, 0)

        def TRIG_COSH(self):
            return self.getToken(ExprParser.TRIG_COSH, 0)

        def TRIG_SINH(self):
            return self.getToken(ExprParser.TRIG_SINH, 0)

        def TRIG_TANH(self):
            return self.getToken(ExprParser.TRIG_TANH, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_trig

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrig" ):
                listener.enterTrig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrig" ):
                listener.exitTrig(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrig" ):
                return visitor.visitTrig(self)
            else:
                return visitor.visitChildren(self)




    def trig(self):

        localctx = ExprParser.TrigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_trig)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 65280) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         




