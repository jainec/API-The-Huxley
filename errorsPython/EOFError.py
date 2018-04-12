# -*- coding: utf-8 -*-

class EOFE(object):

    msg = ""
    id = "EOFError"
    EOFReadingLine = {}
 
    def __init__(self, msg):
        self.msg = msg
        self.EOFReadingLine = {"EOF when reading a line":self.EOFReadingLineFunc()}
 
        #self.erro2 = {"erro att 2":self.metodo2()}
    
    '''    Funções    '''
        
    def EOFReadingLineFunc(self):
        return """EOF - end of file (final de arquivo) - ocorreu um erro de final de arquivo ao realizar a leitura dos dados, verifique a declaração do input ou as entradas."""


    '''
    def func2(self):
        return "erro 2"
    '''


    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.EOFReadingLine]}

    
