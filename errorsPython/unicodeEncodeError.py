# -*- coding: utf-8 -*-

class UnicodeEncodeE(object):

    msg = ""
    id = "UnicodeEncodeError"
    cantEndecodeByte = {}
    
    def __init__(self, msg):
        self.msg = msg
        self.cantEndecodeByte = {"codec can't encode character":self.cantEndecodeByteFunc()}

        '''    
        self. = {"":self.()}
        '''

    
    '''    Funções    '''
        
    def cantEndecodeByteFunc(self):
        try:
            return """Não foi possível codificar o código '"""+self.msg.split("'")[4]+"""', pois está utilizando uma outra codificação, verique qual, o mais comum é o utf8 ou latin1."""
        except:
            return ""

    '''
    def (self):
        return """ """

    '''



    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.cantEndecodeByte]}


    
