# -*- coding: utf-8 -*-

class ValueE(object):

    msg = ""
    id = "ValueError"
    invalidLiteral = {}
    notConvert = {}
    needMore = {}
    mathDomain = {}
    emptySeparator = {}
    notList = {}
    incompleteFormat = {}
    emptySequence = {}
    substringNot = {}
    listRemove = {}
    tooManyValue = {} 
    negativePower = {}
    unsupportedFormat = {}
    unknownFormat = {}
    precisionNot = {}
    invalidConversion = {}
    rangeMust = {}
    unmatchedFormat = {}
    complexString = {}
    lacksBlank = {}
    factorialNegative = {}
    attemptSize = {}
    encounteredFormat = {}
    dictionaryElement = {}
    invalidFormat = {}
    formatPrecision = {}
    attributeFormatString = {}
    
    def __init__(self, msg):
        self.msg = msg
        self.invalidLiteral = {"invalid literal for":self.invalidLiteralFunc()}
        self.notConvert = {"could not convert string to float":self.notConvertFunc()}
        self.needMore = {"need more than":self.needMoreFunc()}   
        self.mathDomain = {"math domain error":self.mathDomainFunc()}
        self.emptySeparator = {"empty separator":self.emptySeparatorFunc()}
        self.notList = {"is not in list":self.notListFunc()}
        self.incompleteFormat = {"incomplete format":self.incompleteFormatFunc()}
        self.emptySequence = {"arg is an empty sequence":self.emptySequenceFunc()}
        self.substringNot = {"substring not found":self.substringNotFunc()}
        self.listRemove = {"list.remove(x): x not in list":self.listRemoveFunc()}
        self.tooManyValue = {"too many values to unpack":self.tooManyValueFunc()}
        self.negativePower = {"negative number cannot be raised to a fractional power":self.negativePowerFunc()}
        self.unsupportedFormat = {"unsupported format character":self.unsupportedFormatFunc()}
        self.unknownFormat = {"Unknown format code ":self.unknownFormatFunc()}
        self.precisionNot = {"Precision not allowed in integer format specifier":self.precisionNotFunc()}
        self.invalidConversion = {"Invalid conversion specification":self.invalidConversionFunc()}
        self.rangeMust = {"must not be zero":self.rangeMustFunc()}
        self.unmatchedFormat = {"unmatched '{' in format":self.unmatchedFormatFunc()}
        self.complexString = {"complex() arg is a malformed string":self.complexStringFunc()}
        self.lacksBlank = {"lacks blank after":self.lacksBlankFunc()}
        self.factorialNegative = {"not defined for negative values":self.factorialNegativeFunc()}
        self.attemptSize = {"attempt to assign sequence of size":self.attemptSizeFunc()}
        self.encounteredFormat = {"encountered in format string":self.encounteredFormatFunc()}
        self.dictionaryElement = {"dictionary update sequence element":self.dictionaryElementFunc()}
        self.invalidFormat = {"Invalid format specifier":self.invalidFormatFunc()}
        self.formatPrecision = {"Format specifier missing precision":self.formatPrecisionFunc()}
        self.attributeFormatString = {"attribute in format string":self.attributeFormatStringFunc()}

        #self.var = {"chave":self.metodo()}

    
    '''    Funções    '''
        
    def invalidLiteralFunc(self):
        try:
            t = self.msg.split("()")[0].replace(" invalid literal for", "")
            v = self.msg.split(":")[1]
            return """O comando"""+ t +"""() necessita de literais compatíveis com seu tipo, verifique os tipos ou dados de leitura: """+v
        except:
            return ""

    def notConvertFunc(self):
        try:
            v = self.msg.split(":")[1]
            return """Não é possível converter o tipo string para float, verique se os dados de leitura são do tipo float: """+v
        except:
            return ""
    
    
    def needMoreFunc(self):
        try:    
            v = self.msg.split("need more than")[1].split("value")[0]
            return """ É necessário ter mais que"""+v+("valor" if int(v) == 1 else "valores")+""", verifique a quantidade de valores da atribuição."""
        except:
            return ""
    
    def mathDomainFunc(self):
        return """Foi feito o uso de função matemática e atribuído um número que não está em seu domínio, geralmente números negativos ou zero. Verifique a expressão de entrada e seu valor."""


    def emptySeparatorFunc(self):
        return """Foi usado um separador vazio para dividir um determinado dado, modifique o parâmetro do separador."""


    def notListFunc(self):
        t = self.msg.replace(" is not in list", "")
        return t+""" não é uma lista, por isso não é possível acessar especificando uma posição, tente modificar o código e retirar o índice de acesso."""


    def incompleteFormatFunc(self):
        return """A formatação está incompleta, verifique a quantidade de "%" em seu código."""

    
    def emptySequenceFunc(self):
        return """Os argumentos da função """+("max()" if "max" in self.msg else "min()")+""" não estão no formato correto, são necessários pelo menos dois argumentos."""


    def substringNotFunc(self):
        return """ O .index() não encontrou o item solicitado. Verifique os dados ao usar o .index() ou tente utilizar o comando str.startswith()."""


    def listRemoveFunc(self):
        return """O parâmetro do comando remove() não está na lista, tente verificar seu tipo e modificá-lo, pois não é possível remover elementos que não estão na lista."""
                  
    
    def tooManyValueFunc(self):
        return """Não é possível descompactar ou atribuir uma tupla que possui mais valores que as variáveis de destino. Verifique a quantidade de variáveis."""


    def negativePowerFunc(self):
        return """Número negativo não pode ser elevado a uma potência fracionária."""

    
    def unsupportedFormatFunc(self):
        try:
            return """O caractere """+ self.msg.split("'")[1] +""" não é válido neste contexto. Verifique se seu uso está correto."""
        except:
            return ""

    
    def unknownFormatFunc(self):
        try:
            l = self.msg.split("'")
            cod = l[1]
            ty = l[3]
            return """A formatação do código """+cod+""" é desconhecida para o tipo do objeto """+ty+""". Verifique seus tipos."""
        except:
            return ""

    
    def precisionNotFunc(self):
        return """Para imprimir um número como ponto flutuante é necessário ter pelo um dos número deste tipo. Verifique se não está tentando imprimir um número inteiro como real ou os argumentos do comando format()."""


    def invalidConversionFunc(self):
        return """A especificação para conversão ou formação foi usada de forma errada, verifique os parâmetro e sua declaração."""


    def rangeMustFunc(self):
        return """Foi utilizado mais de um argumento no comando range(), verifique seus parâmetros."""


    def unmatchedFormatFunc(self):
        return """O caractere '{' é incompatível na formatação, verifique se não é necessário substituir por (."""


    def complexStringFunc(self):
        return """O argumento da função complex() é uma string, é necessário que seja uma parte real e uma parte imaginária, da forma: complex([real[, imag]])."""


    def lacksBlankFunc(self):
        return """Falta um espaço em branco no código especificado depois do : ' ."""


    def factorialNegativeFunc(self):
        return """A função factorial() não é especificada para números negativos, reveja as regras de cálculo de fatorial e o valor do parâmetro passado."""


    def attemptSizeFunc(self):
        return """Foi feita a tentativa de atribuir uma sequência de tamanho 1 a uma de tamanho 2, os tamanhos devem ser equivalentes."""


    def encounteredFormatFunc(self):
        return """Um único caractere '}' foi encontrado na formatação de uma string, verifique se não é necessário substituir por ]."""


    def dictionaryElementFunc(self):
        return """O elemento da sequência de atualização do dicionário tem tamanho 1 e é necessário ter tamanho 2."""


    def invalidFormatFunc(self):
        return """O formato especificado é inválido, verifique os parâmetros do comando format(), por exemplo: format(valor, especificação) ou "string".format(especificação)."""


    def formatPrecisionFunc(self):
        return """A especificação do comando 'format' está faltando o parâmetro precisão. Insira a precisão de formatação para corrigir o erro, por exemplo: format(valor, especificação) ou "string".format(especificação)."""
    
    
    def attributeFormatStringFunc(self):
        return """Foi passado um atributo vazio para formatação de uma string. Verifique os atributos do comando 'format', por exemplo: format(valor, especificação) ou "string".format(especificação)."""


    '''
    def func(self):
        return
    '''
   
   
    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.invalidLiteral, self.notConvert, self.needMore, self.mathDomain, self.emptySeparator,
                         self.notList, self.incompleteFormat, self.emptySequence, self.substringNot, self.listRemove,
                         self.tooManyValue, self.negativePower, self.unsupportedFormat, self.unknownFormat,
                         self.precisionNot, self.invalidConversion, self.rangeMust, self.unmatchedFormat,
                         self.complexString, self.lacksBlank, self.factorialNegative, self.attemptSize,
                         self.encounteredFormat, self.dictionaryElement, self.invalidFormat, self.formatPrecision,
                         self.attributeFormatString]}

