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


    # Enter a parse tree produced by ExprParser#numberExpr.
    def enterNumberExpr(self, ctx:ExprParser.NumberExprContext):
        pass

    # Exit a parse tree produced by ExprParser#numberExpr.
    def exitNumberExpr(self, ctx:ExprParser.NumberExprContext):
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



del ExprParser