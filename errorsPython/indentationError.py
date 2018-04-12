# -*- coding: utf-8 -*-

class IndentationE(object):

    msg = ""
    id = "IndentationError"
    indentedBlock = {}
    unexpectedIndent = {}
    unindentDontMatch = {}
    missingParentheses = {}
    unexpectedUnindent = {}
    
    def __init__(self, msg):
        self.msg = msg
        self.indentedBlock = {"expected an indented block":self.indentedBlockFunc()}
        self.unexpectedIndent = {"unexpected indent":self.unexpectedIndentFunc()}
        self.unindentDontMatch = {"unindent does not match":self.unindentDontMatchFunc()}
        self.missingParentheses = {"Missing parentheses in call to":self.missingParenthesesFunc()}
        self.unexpectedUnindent = {"unexpected unindent":self.unexpectedUnindentFunc()}
        
        '''
        self. = {"":self.()}
        '''
    
    '''    Funções    '''
    
    def indentedBlockFunc(self):
        return """Era esperado um bloco indentado, por favor verifique a indentação. A indentação é uma característica peculiar na linguagem. Enquanto que os blocos são delimitados explicitamente em C, Java e PHP por chaves e em Pascal e Fortran por palavras-chave como then e endif, em Python blocos são delimitados por espaços ou tabulações formando uma indentação visual. Não existem símbolos de “abre” e “fecha”. Fique atento para não errar na próxima!"""

    
    def unexpectedIndentFunc(self):
        return """Indentação inesperada, por favor verifique a indentação. A indentação é uma característica peculiar na linguagem. Enquanto que os blocos são delimitados explicitamente em C, Java e PHP por chaves e em Pascal e Fortran por palavras-chave como then e endif, em Python blocos são delimitados por espaços ou tabulações formando uma indentação visual. Não existem símbolos de “abre” e “fecha”. Fique atento para não errar na próxima!"""


    def unindentDontMatchFunc(self):
        return """A indentação não corresponde a nenhum nível de indentação externa, por favor verifique a indentação. A indentação é uma característica peculiar na linguagem. Enquanto que os blocos são delimitados explicitamente em C, Java e PHP por chaves e em Pascal e Fortran por palavras-chave como then e endif, em Python blocos são delimitados por espaços ou tabulações formando uma indentação visual. Não existem símbolos de “abre” e “fecha”. Fique atento para não errar na próxima!"""

    
    def missingParenthesesFunc(self):
        return """É obrigatório o uso de parênteses a partir da versão 3.0 do Python, insira-os no comando 'print' para solucionar o problema."""

    
    def unexpectedUnindentFunc(self):
        return """Indentação inesperada, por favor verifique a indentação ou se o comando usado realmente está completo. A indentação é uma característica peculiar na linguagem. Enquanto que os blocos são delimitados explicitamente em C, Java e PHP por chaves e em Pascal e Fortran por palavras-chave como then e endif, em Python blocos são delimitados por espaços ou tabulações formando uma indentação visual. Não existem símbolos de “abre” e “fecha”. Fique atento para não errar na próxima!"""

    
    '''
    def (self):
        return """ """
    '''


    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.indentedBlock, self.unexpectedIndent, self.unindentDontMatch, self.missingParentheses, self.unexpectedUnindent]}

    