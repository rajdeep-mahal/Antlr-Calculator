# Generated from Expr.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#infixExpr.
    def enterInfixExpr(self, ctx:ExprParser.InfixExprContext):
        pass

    # Exit a parse tree produced by ExprParser#infixExpr.
    def exitInfixExpr(self, ctx:ExprParser.InfixExprContext):
        pass


    # Enter a parse tree produced by ExprParser#termExpr.
    def enterTermExpr(self, ctx:ExprParser.TermExprContext):
        pass

    # Exit a parse tree produced by ExprParser#termExpr.
    def exitTermExpr(self, ctx:ExprParser.TermExprContext):
        pass


    # Enter a parse tree produced by ExprParser#trigExpr.
    def enterTrigExpr(self, ctx:ExprParser.TrigExprContext):
        pass

    # Exit a parse tree produced by ExprParser#trigExpr.
    def exitTrigExpr(self, ctx:ExprParser.TrigExprContext):
        pass


    # Enter a parse tree produced by ExprParser#parensExpr.
    def enterParensExpr(self, ctx:ExprParser.ParensExprContext):
        pass

    # Exit a parse tree produced by ExprParser#parensExpr.
    def exitParensExpr(self, ctx:ExprParser.ParensExprContext):
        pass


    # Enter a parse tree produced by ExprParser#exponentialExpr.
    def enterExponentialExpr(self, ctx:ExprParser.ExponentialExprContext):
        pass

    # Exit a parse tree produced by ExprParser#exponentialExpr.
    def exitExponentialExpr(self, ctx:ExprParser.ExponentialExprContext):
        pass


    # Enter a parse tree produced by ExprParser#factorialExpression.
    def enterFactorialExpression(self, ctx:ExprParser.FactorialExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#factorialExpression.
    def exitFactorialExpression(self, ctx:ExprParser.FactorialExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#exponential.
    def enterExponential(self, ctx:ExprParser.ExponentialContext):
        pass

    # Exit a parse tree produced by ExprParser#exponential.
    def exitExponential(self, ctx:ExprParser.ExponentialContext):
        pass


    # Enter a parse tree produced by ExprParser#term.
    def enterTerm(self, ctx:ExprParser.TermContext):
        pass

    # Exit a parse tree produced by ExprParser#term.
    def exitTerm(self, ctx:ExprParser.TermContext):
        pass


    # Enter a parse tree produced by ExprParser#trig.
    def enterTrig(self, ctx:ExprParser.TrigContext):
        pass

    # Exit a parse tree produced by ExprParser#trig.
    def exitTrig(self, ctx:ExprParser.TrigContext):
        pass



del ExprParser