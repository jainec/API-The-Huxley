# -*- coding: utf-8 -*-

class PermissionE(object):

    msg = ""
    id = "PermissionError"
    permissionDenied = {}

    def __init__(self, msg):
        self.msg = msg
        self.permissionDenied = {"Permission denied":self.permissionDeniedFunc()}

        '''    
        self. = {"":self.()}
        '''

    
    '''    Funções    '''
        
    def permissionDeniedFunc(self):
        try:
            return """Não foi possivel abrir o diretório no caminho: '"""+self.msg.split("'")[1]+"""', verifique-o. Tente colocar duas barras ou modificar o caminho, por exemplo: caminho = "..\\\Pasta\\\Arquivo.txt"."""
        except:
            return ""

    '''
    def (self):
        return """ """

    '''



    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.permissionDenied]}


    
