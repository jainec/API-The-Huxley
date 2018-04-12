# -*- coding: utf-8 -*-

class OverflowE(object):

    msg = ""
    id = "OverflowError"
    largeConvert = {}
    resultOutRange = {}
    divisionLarge = {}

    def __init__(self, msg):
        self.msg = msg
        self.largeConvert = {"too large to convert to":self.largeConvertFunc()}
        self.resultOutRange = {"Numerical result out of range":self.resultOutRangeFunc()}
        self.divisionLarge = {"division result too large for":self.divisionLargeFunc()}
        
        '''    
        self. = {"":self.()}
        '''

    
    '''    Funções    '''
        
    def largeConvertFunc(self):
        return """O inteiro é muito grande para ser convertido para float, verifique o tamanho do inteiro antes de tentar converter ou tente usar a biblioteca Decimal()."""


    def resultOutRangeFunc(self):
        return """O resultado numérico está fora de seu intervalo permitido, verifique seu intervalo."""


    def divisionLargeFunc(self):
        return """O resultado da divisão inteira é muito grande para ser atribuído a um número ponto flutuante, verifique seu tamanho."""


    '''
    def (self):
        return """ """
    '''



    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.largeConvert, self.resultOutRange, self.divisionLarge]}


    
