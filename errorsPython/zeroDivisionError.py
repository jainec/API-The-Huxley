# -*- coding: utf-8 -*-

class ZeroDivisionE(object):

    msg = ""
    id = "ZeroDivisionError"
    divisionByZero = {}
    moduloByZero = {}
    floatModulo = {}
    floatDivmod = {}

    def __init__(self, msg):
        self.msg = msg
        self.divisionByZero = {"division by zero":self.divisionByZeroFunc()}
        self.moduloByZero = {"division or modulo by zero":self.moduloByZeroFunc()}
        self.floatModulo = {"float modulo":self.floatModuloFunc()}
        self.floatDivmod = {"float divmod()":self.floatDivmodFunc()}
        
        '''    
        self. = {"":self.()}
        '''

    
    '''    Funções    '''
        
    def divisionByZeroFunc(self):
        return """Não é possível realizar divisão por zero, verifique se isso ocorre em seu código."""


    def moduloByZeroFunc(self):
        return """Não é possível realizar divisão ou módulo por zero, verifique se isto ocorre em seu código."""


    def floatModuloFunc(self):
        return """Não é possível realizar divisão ou módulo por zero. Somente é possível calcular o módulo entre números inteiros. Verifique se isto ocorre em seu código."""


    def floatDivmodFunc(self):
        return """Não é possível realizar divisão ou módulo por zero. Somente é possível calcular o módulo entre números inteiros. Verifique se isto ocorre em seu código."""


    '''
    def (self):
        return """ """

    '''



    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.divisionByZero, self.moduloByZero, self.floatModulo, self.floatDivmod]}


    
