grammar Expr;

prog: expr EOF;

expr: expr op expr           #infixExpr
| exponential expr               #expoExpr
| trigFunc '(' expr ')'         #trigExpr
| term                          #numberExpr
| '(' expr ')'                  #parensExpr
| fact_expr                     #factorialExpr
;


exponential: LOG_BASE_10
| NATURAL_LOG
| SQRT
| CUBE_RT
;

fact_expr: term '!'
;

term:
| INT
| DEC
| PI
| EULER
;




trigFunc: TRIG_COS
| TRIG_SIN
| TRIG_TAN
| TRIG_DEG
| TRIG_RAD
| TRIG_COSH
| TRIG_SINH
| TRIG_TANH
;

op: OP_ADD
| OP_SUB
| OP_DIV
| OP_MUL
| OP_POW
| OP_MOD
;


LOG_BASE_10: 'log₁₀';
SQRT: '√';
CUBE_RT: [chr(8731)];
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