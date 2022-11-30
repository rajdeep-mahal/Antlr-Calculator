import math

from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
from math import *

class MyExprVisitor(ExprVisitor):
    def __init__(self):
        super(MyExprVisitor, self).__init__()
        self.stack = []  # Stack to evaluate the expression

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx: ExprParser.ProgContext):
        return self.visit(ctx.expr())  # Just visit the self expression

    # Visit a parse tree produced by ExprParser#infixExpr.
    def visitInfixExpr(self, ctx: ExprParser.InfixExprContext):
        self.visit(ctx.left)  # Evaluate the left  expression and push to stack
        self.visit(ctx.right)  # Evaluate the right expression and push to stack

        b = self.stack.pop()  # Why is ‘b’ the first popped item?
        a = self.stack.pop()
        c = None

        if ctx.OP_ADD():
            c = a + b
        elif ctx.OP_SUB():
            c = a - b
        elif ctx.OP_MUL():
            c = a * b
        elif ctx.OP_DIV():
            c = a / b
        elif ctx.OP_POW():
            c = pow(a, b)
        elif ctx.OP_MOD():
            c = a % b

        self.stack.append(c)
        return c

    def visitTermExpr(self, ctx:ExprParser.TermExprContext):
        if ctx.term().INT():
            c = int(str(ctx.term().INT()))  # Found a number, just insert to stack
            self.stack.append(c)
            return c
        elif ctx.term().PI():
            c = pi
            self.stack.append(c)
            return c
        elif ctx.term().DEC():
            c = float(str(ctx.term().DEC()))
            self.stack.append(c)
            return c
        elif ctx.term().EULER():
            c = math.e
            self.stack.append(c)
            return c

    def visitExponentialExpr(self, ctx: ExprParser.ExponentialExprContext):
        self.visit(ctx.expr())
        c = self.stack.pop()
        if ctx.exponential().LOG_BASE_10():
            self.stack.append(log10(c))
            return log10(c)
        elif ctx.exponential().NATURAL_LOG():
            self.stack.append(log(c))
            return log(c)
        elif ctx.exponential().SQRT():
            self.stack.append(c ** (1./2.))
            return c ** (1./2.)
        elif ctx.exponential().CUBE_RT():
            self.stack.append(c ** (1. / 3.))
            return c ** (1. / 3.)

    def visitFactorialExpression(self, ctx:ExprParser.FactorialExpressionContext):
        self.visit(ctx.expr())
        c = self.stack.pop()
        self.stack.append(factorial(c))
        return factorial(c)

    def visitTrigExpr(self, ctx: ExprParser.TrigExprContext):
       self.visit(ctx.expr())
       c = self.stack.pop()

       if ctx.trig().TRIG_SIN():
           self.stack.append(sin(c))
           return sin(c)

       elif ctx.trig().TRIG_COS():
           self.stack.append(cos(c))
           return cos(c)

       elif ctx.trig().TRIG_TAN():
           self.stack.append(tan(c))
           return tan(c)

       elif ctx.trig().TRIG_RAD():
           self.stack.append(radians(c))
           return radians(c)

       elif ctx.trig().TRIG_COSH():
           self.stack.append(cosh(c))
           return cosh(c)

       elif ctx.trig().TRIG_SINH():
           self.stack.append((sinh(c)))
           return sinh(c)

       elif ctx.trig().TRIG_TANH():
           self.stack.append((tanh(c)))
           return tanh(c)

       elif ctx.trig().TRIG_DEG():
           self.stack.append((degrees(c)))
           return degrees(c)


    # Visit a parse tree produced by ExprParser#parensExpr.
    def visitParensExpr(self, ctx: ExprParser.ParensExprContext):
        return self.visit(ctx.expr())  # Since enclosed by parents, just visit expr