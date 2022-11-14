from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
from math import sin, cos, tan, pi

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

        self.stack.append(c)
        return c

    # Visit a parse tree produced by ExprParser#numberExpr.
    def visitNumberExpr(self, ctx: ExprParser.NumberExprContext):
        if ctx.INT():
            c = int(str(ctx.INT()))  # Found a number, just insert to stack
        elif ctx.PI():
            c = pi
        elif ctx.DEC():
            c = float(str(ctx.DEC()))
        self.stack.append(c)
        return c

    def visitTrigExpr(self, ctx: ExprParser.TrigExprContext):
       self.visit(ctx.expr())
       c = self.stack.pop()
       if ctx.TRIG_SIN():
           self.stack.append(sin(c))
           return sin(c)
       elif ctx.TRIG_COS():
           self.stack.append(cos(c))
           return cos(c)
       elif ctx.TRIG_TAN():
           self.stack.append(tan(c))
           return tan(c)

    # Visit a parse tree produced by ExprParser#parensExpr.
    def visitParensExpr(self, ctx: ExprParser.ParensExprContext):
        return self.visit(ctx.expr())  # Since enclosed by parents, just visit expr