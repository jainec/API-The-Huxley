# -*- coding: utf-8 -*-

class KeyE(object):

    msg = ""
    id = "KeyError"
    keyError = {}

    def __init__(self, msg):
        self.msg = msg
        self.keyError = {self.msg:self.keyErrorFunc()}

        '''    
        self. = {"":self.()}
        '''

    
    '''    Funções    '''
        
    def keyErrorFunc(self):
        return """A chave digitada não é válida, verifique seu tipo ou seu uso:"""+self.msg


    '''
    def (self):
        return """ """

    '''


    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.keyError]}

    
