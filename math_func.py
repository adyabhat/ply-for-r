import ply.lex as lex

# List of token names
reserved = {
   'print' : 'PRINT',
}

tokens = [
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'NUMBER',
    'SIN',
    'COS',
    'TAN',
    'LOG',
    'SQRT',
    'IDENTIFIER',
] + list(reserved.values())

# Regex for the tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

def t_NUMBER(t):
    r'\d+' # At least one digit, any number of times after that
    t.value = float(t.value) # Making it of appropriate datatype
    return t

# Regular expression rules for simple math functions
def t_SIN(t):
    r'sin'
    return t

def t_COS(t):
    r'cos'
    return t

def t_TAN(t):
    r'tan'
    return t

def t_LOG(t):
    r'log'
    return t

def t_SQRT(t):
    r'sqrt'
    return t

def t_IDENTIFIER(t):
    r'[.][._a-zA-Z]* | [a-zA-Z][a-zA-Z0-9._]*'
    t.type = reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
    return t

# To track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.yacc as yacc

def p_expression(p):
    '''
    expression : NUMBER
               | IDENTIFIER
               | expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | SIN LPAREN expression RPAREN
               | COS LPAREN expression RPAREN
               | TAN LPAREN expression RPAREN
               | LOG LPAREN expression RPAREN
               | SQRT LPAREN expression RPAREN
               | LPAREN expression RPAREN
    '''
    p[0] = "\nThe given 'mathematical expression' is valid."

# Build the lexer
lexer = lex.lex()

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('\n\ninput > ')
        lexer.input(s)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)