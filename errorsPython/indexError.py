# -*- coding: utf-8 -*-

class IndexE(object):

    msg = ""
    id = "IndexError"
    indexRange = {}
    popEmptyList = {}
    
    def __init__(self, msg):
        self.msg = msg
        self.indexRange = {"index out of range":self.indexRangeFunc()}
        self.popEmptyList = {"pop from empty list":self.popEmptyListFunc()}

        '''    
        self. = {"":self.()}
        '''
    
    '''    Funções    '''
        
    def indexRangeFunc(self):
        return """O índice da lista está fora do intervalo, verique o índice de acesso e seu valor."""


    def popEmptyListFunc(self):
        return """A lista está vazia, por isso não é possível utilizar o comando pop(). Só é possível utilizar se a lista possuir tamanho maior ou igual a um."""


    '''
    def (self):
        return """ """

    '''


    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.indexRange, self.popEmptyList]}

    
