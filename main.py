import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor


def main(argv):
    input = InputStream("sin 4^3")

    lexer = ExprLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()

    res = MyExprVisitor().visitProg(tree)  # Evaluate the expression

    print(input, '=', res)


if __name__ == '__main__':
    main(sys.argv)