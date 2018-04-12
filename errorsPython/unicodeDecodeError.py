# -*- coding: utf-8 -*-

class UnicodeDecodeE(object):

    msg = ""
    id = "UnicodeDecodeError"
    decodeByte = {}
    
    def __init__(self, msg):
        self.msg = msg
        self.decodeByte = {"codec can't decode byte":self.decodeByteFunc()}

        '''    
        self. = {"":self.()}
        '''

    
    '''    Funções    '''
        
    def decodeByteFunc(self):
        try:
            return """Não foi possível decodificar o código '"""+self.msg.split("byte")[1].split("in")[0]+"""', pois está utilizando uma outra decodificação, verique qual, o mais comum é o utf8 ou latin1."""
        except:
            return ""

    '''
    def (self):
        return """ """
    '''



    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.decodeByte]}

