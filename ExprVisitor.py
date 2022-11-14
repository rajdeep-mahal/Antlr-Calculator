# Generated from Expr.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#infixExpr.
    def visitInfixExpr(self, ctx:ExprParser.InfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#numberExpr.
    def visitNumberExpr(self, ctx:ExprParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#trigExpr.
    def visitTrigExpr(self, ctx:ExprParser.TrigExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parensExpr.
    def visitParensExpr(self, ctx:ExprParser.ParensExprContext):
        return self.visitChildren(ctx)



del ExprParser