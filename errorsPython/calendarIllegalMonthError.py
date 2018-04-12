# -*- coding: utf-8 -*-

class IllegalMonthE(object):

    msg = ""
    id = "calendar.IllegalMonthError"
    badMonthNumber = {}

    def __init__(self, msg):
        self.msg = msg
        self.badMonthNumber = {"bad month number":self.badMonthNumberFunc()}

        '''    
        self. = {"":self.()}
        '''

    
    '''    Funções    '''
        
    def badMonthNumberFunc(self):
        return """O formato do mês está errado, deve ser um número entre 1-12, representando os meses do ano."""


    '''
    def (self):
        return """ """
    '''



    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.badMonthNumber]}


    
