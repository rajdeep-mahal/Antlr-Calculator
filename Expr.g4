grammar Expr;

prog: expr EOF;

expr: left=expr op='^' right=expr #infixExpr
    | left=expr op=('*'|'/') right=expr #infixExpr
    | left=expr op=('+'|'-') right=expr #infixExpr
    | INT                                 #numberExpr
    | '(' expr ')'                        #parensExpr
    | op=('sin'|'cos'|'tan') expr         #trigExpr
    ;


TRIG_SIN: 'sin';
TRIG_COS: 'cos';
TRIG_TAN: 'tan';
OP_POW: '^';
OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV: '/';

NEWLINE : [\r\n]+ ;
INT     : [0-9]+ ;
WS      : [ \t\r\n] -> channel(HIDDEN);