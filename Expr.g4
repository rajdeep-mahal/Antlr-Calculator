grammar Expr;

prog: expr EOF;

expr: op=('sin'|'cos'|'tan')'(' expr ')'  #trigExpr
    | left=expr op='^' right=expr #infixExpr
    | left=expr op=('*'|'/') right=expr #infixExpr
    | left=expr op=('+'|'-') right=expr #infixExpr
    | INT                                 #numberExpr
    | DEC                                 #numberExpr
    | PI                                  #numberExpr
    | '(' expr ')'                        #parensExpr
    ;


TRIG_SIN: 'sin';
TRIG_COS: 'cos';
TRIG_TAN: 'tan';
OP_POW: '^';
OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV: '/';
PI: 'pi';
DEC: INT '.' INT;
NEWLINE : [\r\n]+ ;
INT     : [0-9]+ ;
WS      : [ \t\r\n] -> channel(HIDDEN);