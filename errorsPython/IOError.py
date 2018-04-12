# -*- coding: utf-8 -*-

class IOE(object):

    msg = ""
    id = "IOError"
    permissionDdenied = {}

    def __init__(self, msg):
        self.msg = msg
        self.permissionDdenied = {"Permission denied":self.permissionDdeniedFunc()}

        '''    
        self. = {"":self.()}
        '''

    
    '''    Funções    '''
        
    def permissionDdeniedFunc(self):
        try:
            path = self.msg.split(":")[1]
            return """Não é permitido abrir o diretório no caminho: """+path.rstrip()+""", verifique-o. Tente colocar duas barras ou modificar o caminho, por exemplo: caminho = "..\\\Pasta\\\Pasta\\\Arquivo.txt"."""
        except:
            return ""

    '''
    def (self):
        return """ """

    '''



    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.permissionDdenied]}


    
