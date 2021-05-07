grammar xml;

s : element s | ;

element : TAG_START content TAG_END ;

content : element content* | POD content* ;

TAG_START : '<' STR ATTRIB* '>' ;
TAG_END : '</' STR '>' ;

ATTRIB : STR '=' '"' POD '"' ;

POD : NUM | STR | MACRO ;

MACRO : '!' SIGN STR ;

STR : CHAR (CHAR|DIGIT)* ;
fragment CHAR : [a-zA-Z] ;

NUM : SIGN? DIGITS ('.'DIGITS)? ;
fragment DIGITS : DIGIT+ ;
fragment DIGIT : [0-9] ;

SIGN : '+' | '-' ;

WS : [ \t]+ -> skip ;

NL:'\r'? '\n' -> skip ;
