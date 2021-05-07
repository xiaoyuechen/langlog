grammar xml;

s : element s |  ;

element : tagstart content tagend ;

content : element content? | pod content? ;

tagstart : '<' STR WS* attrib* '>' ;
tagend : '</' STR '>' ;

attrib : STR '=' '"' pod '"' ;

pod : NUM | STR | macro ;

macro : '!' SIGN WS* STR ;

STR : CHAR (CHAR|DIGIT)* ;
fragment CHAR : [a-zA-Z] ;

NUM : SIGN? DIGITS ('.'DIGITS)? ;
fragment DIGITS : DIGIT+ ;
fragment DIGIT : [0-9] ;

SIGN : '+' | '-' ;

WS : [ \r\t\n]+ -> skip ;
