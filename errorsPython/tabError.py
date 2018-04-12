# -*- coding: utf-8 -*-

class TabE(object):

    msg = ""
    id = "TabError"
    inconsistentTabs = {}
    missingParentheses = {}
    
    def __init__(self, msg):
        self.msg = msg
        self.inconsistentTabs = {"inconsistent use of tabs":self.inconsistentTabsFunc()}
        self.missingParentheses = {"Missing parentheses in call to":self.missingParenthesesFunc()}
        
        '''    
        self. = {"":self.()}
        '''

    
    '''    Funções    '''
        
    def inconsistentTabsFunc(self):
        return """O uso de tabs e espaços estão inconsistentes, verifique seu uso e sua quantidade."""


    def missingParenthesesFunc(self):
        return """É obrigatório o uso de parênteses a partir da versão 3.0 do Python, insira-os no comando 'print' para solucionar o problema."""


    '''
    def (self):
        return """ """


    def (self):
        return """ """

    '''



    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.inconsistentTabs, self.missingParentheses]}


    
