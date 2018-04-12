# -*- coding: utf-8 -*-

class UnboundLocalE(object):

    msg = ""
    id = "UnboundLocalError"
    referencedBefore = {}

    def __init__(self, msg):
        self.msg = msg
        self.referencedBefore = {"referenced before assignment":self.referencedBeforeFunc()}

        '''    
        self. = {"":self.()}
        '''

    
    '''    Funções    '''
        
    def referencedBeforeFunc(self):
        try:
            val = self.msg.split("'")
            return """Não é possível fazer referência ou uso de uma variável antes dela ser declarada ou atribuída. Verifique o uso da variável '"""+val[1]+"""' ou veja se não é necessário o uso de uma variável global."""
        except:
            return ""

    '''
    def (self):
        return """ """

    '''



    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.referencedBefore]}

    
