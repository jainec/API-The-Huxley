# -*- coding: utf-8 -*-

class FileNotFoundE(object):

    msg = ""
    id = "FileNotFoundError"
    noFileDirectory = {}

    def __init__(self, msg):
        self.msg = msg
        self.noFileDirectory = {"No such file or directory":self.noFileDirectoryFunc()}

        '''    
        self. = {"":self.()}
        '''

    
    '''    Funções    '''
        
    def noFileDirectoryFunc(self):
        try:
            return """Não foi possivel abrir o diretório no caminho: """+self.msg.split(":")[1].rstrip()+""", verifique-o. Tente colocar duas barras ou modificar o caminho, por exemplo: caminho = "..\\\Pasta\\\\"""+self.msg.split("'")[1].replace("/","")+"""."""
        except:
            return ""


    '''
    def (self):
        return """ """

    '''



    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.noFileDirectory]}


    
