# -*- coding: utf-8 -*-

class NameE(object):

    msg = ""
    id = "NameError"
    nameNotDefined = {}

    def __init__(self, msg):
        self.msg = msg
        self.nameNotDefined = {"is not defined":self.ne_NotDefined()}


    '''    Funções    '''

    def ne_NotDefined(self):
        try:
            list_new = self.msg.split()
            var = []
            for i in list_new:
                if "'" in i:
                    var.append(i)
            return """Foi feito o uso de uma variável que não foi definida ou um comando que foi escrito de forma errada. Verifique a palavra """+var[0]+"."
        except:
            return ""

    
    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.nameNotDefined]}
