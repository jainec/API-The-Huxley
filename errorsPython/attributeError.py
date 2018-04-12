# -*- coding: utf-8 -*-

class AttributeE(object):

    msg = ""
    id = "AttributeError"
    objectNotAttribute = {}
    typeObject = {}

    def __init__(self, msg):
        self.msg = msg
        self.objectNotAttribute = {"object has no attribute":self.objectNotAttributeFunc()}
        self.typeObject = {"type object":self.typeObjectFunc()}
        '''    
        self. = {"":self.()}
        '''

    
    '''    Funções    '''
        
    def objectNotAttributeFunc(self):
        try:
            obj = self.msg.split("'")
            return """O objeto do tipo '"""+obj[1]+"""' não tem nenhum atributo com o nome '"""+obj[3]+"""', verifique se digitou corretamente o nome do atributo ou o objeto."""
        except:
            return ""


    def typeObjectFunc(self):
        try:
            obj = self.msg.split("'")
            return """O tipo do objeto '"""+obj[1]+"""' não tem nenhum atributo de nome '"""+obj[3]+"""', verifique se o nome do atributo foi digitado corretamente."""
        except:
            return ""


    '''
    def (self):
        return """ """


    def (self):
        return """ """

    '''



    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.objectNotAttribute, self.typeObject]}


    
