grammar Expr;

prog: expr EOF;

expr: left=expr op='^' right=expr              #infixExpr
| left=expr op=('*' | '/' | '%') right=expr       #infixExpr
| left=expr op=('-' | '+') right=expr       #infixExpr
| exponential '(' expr ')'   #exponentialExpr
| trig '(' expr ')'         #trigExpr
| term                          #termExpr
| '(' expr ')'                  #parensExpr
| '(' expr ')!'                 #factorialExpression
;


exponential: LOG_BASE_10
| NATURAL_LOG
| SQRT
| CUBE_RT
;

term:
| INT
| DEC
| PI
| EULER
;




trig: TRIG_COS
| TRIG_SIN
| TRIG_TAN
| TRIG_DEG
| TRIG_RAD
| TRIG_COSH
| TRIG_SINH
| TRIG_TANH
;

LOG_BASE_10: 'log10';
SQRT: 'sqrt';
CUBE_RT: 'cbrt';
NATURAL_LOG: 'ln';


TRIG_DEG: 'deg';
TRIG_RAD: 'rad';
TRIG_COSH: 'cosh';
TRIG_SINH: 'sinh';
TRIG_TANH: 'tanh';
TRIG_SIN: 'sin';
TRIG_COS: 'cos';
TRIG_TAN: 'tan';


OP_POW: '^';
OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV: '/';
OP_MOD: '%';

PI: 'pi';
EULER: 'e';
DEC: INT '.' INT;
NEWLINE : [\r\n]+ ;
INT     : [0-9]+ ;
WS      : [ \t\r\n] -> channel(HIDDEN);