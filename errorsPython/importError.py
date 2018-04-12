# -*- coding: utf-8 -*-

class ImportE(object):

    msg = ""
    id = "ImportError"
    noModuleNamed = {}
    cannotImport = {}

    def __init__(self, msg):
        self.msg = msg
        self.noModuleNamed = {"No module named":self.noModuleNamedFunc()}
        self.cannotImport = {"cannot import name":self.cannotImportFunc()}

        '''    
        self. = {"":self.()}
        self. = {"":self.()}
        '''

    
    '''    Funções    '''
        
    def noModuleNamedFunc(self):
        try:
            return """Ocorreu um erro ao importar o módulo, pois não foi encontrado nenhum módulo com o nome '"""+self.msg.split("'")[1]+"""', verifique se digitou corretamente, se realmente existe ou se este módulo requer instalação."""
        except:
            return ""


    def cannotImportFunc(self):
        try:
            return """Não foi possível importar a biblioteca de nome '"""+self.msg.split("'")[1]+"""'. Verifique se digitou corretamente, se ela realmente existe ou se não é necessário algum arquivo de configuração ou instalação."""
        except:
            return ""


    '''
    def (self):
        return """ """

    '''



    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.noModuleNamed, self.cannotImport]}

    
