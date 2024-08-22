# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:26:27 2023

@author: Chandana B S
"""

import ply.lex as lex

# list of token names
reserved = {
   'print' : 'PRINT',
   'if' : 'IF',
   'else' : 'ELSE',
}

tokens = [
    # don't include reserve words here, since they are 
    # added through the reserved words tuple-list
    'EQUALITYCHECK',
    'EQUALS',
    'ASSIGN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'NUMBER',
    'IDENTIFIER',
    'STRING',
    'GORE',
    'LORE',
    'LESSTHAN',
    'GREATERTHAN',
    'SEMICOLON'
] + list(reserved.values())

# regex for the tokens
t_ASSIGN = r'<-'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_EQUALITYCHECK = r'=='
t_EQUALS  = r'='
t_LORE = r'<='
t_GORE = r'>='
t_GREATERTHAN = r'>'
t_LESSTHAN = r'<'
t_SEMICOLON = r';'

def t_NUMBER(t):
    r'\d+' # at least one digit, any number of times after that
    t.value = float(t.value) # making it of appropriate datatype
    return t

def t_IDENTIFIER(t):
    r'[.][._a-zA-Z]* | [a-zA-Z][a-zA-Z0-9._]*'
    t.type = reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
    return t

def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    return t
    
# to track line numbers
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

def p_if_else_statement(p):
    '''
    if_else_statement : IF LPAREN cond_exp RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE
                      | IF LPAREN cond_exp RPAREN LBRACE statement RBRACE ELSE statement
                      | IF LPAREN cond_exp RPAREN statement ELSE LBRACE statement RBRACE
                      | IF LPAREN cond_exp RPAREN statement ELSE statement
    '''
    p[0] = "\nThe given 'if-else' statement is valid."
    
def p_cond_expression(p):
    '''
    cond_exp : alg_exp GREATERTHAN alg_exp
             | alg_exp LESSTHAN alg_exp
             | alg_exp GORE alg_exp
             | alg_exp LORE alg_exp
             | alg_exp EQUALITYCHECK alg_exp
    '''
    pass

def p_alg_expression(p):
    '''
    alg_exp : IDENTIFIER
            | NUMBER
            | alg_exp PLUS alg_exp
            | alg_exp MINUS alg_exp
            | alg_exp TIMES alg_exp
            | alg_exp DIVIDE alg_exp
    '''
    pass



def p_statement(p):
    '''
    statement : SEMICOLON
            | if_else_statement
            | statement statement
            | assignment_statement
            | print_statement
    '''
    pass

def p_assignment_statement(p):
    '''
    assignment_statement : IDENTIFIER ASSIGN alg_exp
                        | IDENTIFIER EQUALS alg_exp
    '''
    pass

def p_print_statement(p):
    '''
    print_statement : PRINT LPAREN print_enclosed RPAREN
    '''
    pass

def p_print_enclosed(p):
    '''
    print_enclosed : IDENTIFIER PLUS print_enclosed
                | STRING PLUS print_enclosed
                | alg_exp
                | STRING
    '''
    pass

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
   if not s: continue
   result = parser.parse(s)
   print(result)    