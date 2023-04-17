//ID: 2013736
grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

// LEXER
WS: [ \t\r\n] -> skip;
COMMENT: '/*' .*? '*/' -> skip;
INLINE_COMMENT: '//' ~[\r\n]* -> skip;

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';

NOT: '!';
AND: '&&';
OR: '||';
EQ: '==';

NEQ: '!=';
LT: '<';
LTEQ: '<=';
GT: '>';
GTEQ: '>=';
STRCON: '::';

LP: '(';
RP: ')';
LS: '[';
RS: ']';
LB: '{';
RB: '}';
DOT: '.';
COMMA: ',';
SEMI: ';';
COL: ':';
ASSIGN: '=';

AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';

ID: [a-zA-Z_][a-zA-Z_0-9]*;

fragment INTPART: [0-9]+;
fragment DECPART: '.' [0-9]*;
fragment EXPPART: [Ee] [+-]? INTPART;
INTLIT:
	'0'
	| [1-9] [0-9]* ('_' INTPART)*
	{self.text = self.text.replace('_', '')};
FLOATLIT:
	(INTLIT DECPART | INTLIT DECPART? EXPPART | DECPART EXPPART)
	{self.text = self.text.replace('_', '')};

STRINGLIT: '"' STRING_CHAR*? '"'
	{self.text = self.text[1:]; self.text = self.text[:-1]};

fragment ESC_CHAR: '\\' [bfrnt'"\\];
fragment STRING_CHAR: ~[\n"'\\] | ESC_CHAR;


UNCLOSE_STRING: '"' STRING_CHAR* ('\n'|EOF)
{
s = str(self.text)
if s[-1] == '\n': 
	raise UncloseString(s[1:-2]) 
else: 
	raise UncloseString(s[1:])
};

fragment ILLEGAL_CHAR: '\\' ~[bfrnt'"\\];
ILLEGAL_ESCAPE: '"' STRING_CHAR* ILLEGAL_CHAR {raise IllegalEscape(self.text[1:])};

ERROR_CHAR: . {raise ErrorToken(self.text)};
// END OF LEXER



// PARSER
program: decl+ EOF;
decl: funcDecl | varDecl;

funcDecl: 
	ID COL FUNCTION (VOID | typ) LP paramlist RP (INHERIT ID)? 
	blockStmt;

varDecl: idlist COL typ SEMI | varDeclFull SEMI;
varDeclFull: 
	ID COMMA varDeclFull COMMA expr 
	| ID COL typ ASSIGN expr;

idlist: ID COMMA idlist | ID;

// Function calls
param: INHERIT? OUT? ID COL typ;
paramPrime: param COMMA paramPrime | param;
paramlist: paramPrime |;

arglist: exprlist |;
funcCall: ID LP arglist RP;

dimensionlist: INTLIT COMMA dimensionlist | INTLIT;
atomicTyp: INTEGER | FLOAT | BOOLEAN | STRING;
arrayTyp: ARRAY LS dimensionlist RS OF atomicTyp;
typ: atomicTyp | AUTO | arrayTyp;

// Expressions
operand: typelit | ID | funcCall;

indexOp: ID LS exprlist RS;
signOp: MINUS;
logicalOp: NOT;
multiplyingOp:  DIV | MULT | MOD;
addingOp: MINUS | PLUS;
logicalBinaryOp: AND | OR;
relationalOp: EQ | NEQ | LT | LTEQ | GT | GTEQ;
stringOp: STRCON;

expr: 
	LP expr RP 
	| <assoc=left> indexOp
	| <assoc=right> signOp expr
	| <assoc=right> logicalOp expr
	| <assoc=left> expr multiplyingOp expr
	| <assoc=left> expr addingOp expr
	| <assoc=left> expr logicalBinaryOp expr
	| expr relationalOp expr // none-assoc
	| expr stringOp expr //none-asso
	| operand
	;

exprlist: expr COMMA exprlist | expr;

// Statements
stmt: 
	assignmentStmt 
	| ifStmt 
	| forStmt 
	| whileStmt 
	| doWhileStmt 
	| breakStmt 
	| continueStmt 
	| returnStmt 
	| callStmt
	| blockStmt;

	blockStmtElement: stmt | varDecl;
	blockStmtElements: blockStmtElement blockStmtElements |;
	blockStmt: LB blockStmtElements RB;


	assignmentStmt: (indexOp | ID) ASSIGN expr SEMI;
	ifStmt: IF LP expr RP stmt elseStmt?;
		elseStmt: ELSE stmt;
	forStmt: FOR LP ID ASSIGN expr COMMA expr COMMA expr RP stmt;
	whileStmt: WHILE LP expr RP stmt;
	doWhileStmt:
		DO blockStmt
		WHILE LP expr RP SEMI;
	breakStmt: BREAK SEMI;
	continueStmt: CONTINUE SEMI;
	returnStmt: RETURN expr SEMI | RETURN SEMI;
	callStmt: funcCall SEMI;


// Literals
typelit: INTLIT | FLOATLIT | STRINGLIT | arraylit | TRUE | FALSE;
	arraylit: 
		LB exprlist RB 
		| LB RB;
// END OF PARSER
