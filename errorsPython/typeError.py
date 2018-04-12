# -*- coding: utf-8 -*-

class TypeE(object):

    msg = ""
    id = "TypeError"
    unsupportedOperand = {}
    objectNotIterable = {}
    unorderableTypes = {}
    objectNoAttribute = {}
    notAllArgs = {}
    objectNotCallable = {}
    objectNotSubscriptable = {}
    cantMultiplyStr = {}
    objectCannotInteger = {}
    argumentMustNumber = {}
    objectToImplicitly = {}
    listMustIntegers = {}
    hasNoLen = {}
    aBytesObjectNumber = {}
    cannotConcatenate = {}
    integerArgsExpected = {}
    aFloatRequired = {}
    floatArgumentRequired = {}
    cantConvertComplex = {}
    takesExactly = {}
    formatANnumber = {}
    notFormatString = {}
    canOnlyConcatenate = {}
    objectNotSupport = {}
    requiredArgument = {}
    invalidKeyword = {}
    sliceIndices = {}
    badUnary = {}
    sequenceItem = {}
    takesMost = {}
    takesNoArguments = {}
    takesLeastArgument = {}
    argumentType = {}
    unhashableType = {}
    nonFormat = {}
    objectButReceived = {}
    expectedBuffer = {}
    expectedAtMost = {}
    positionalArguments = {}
    cantConvertInt = {}
    objectNeedsArgument = {}
    expectedAtLeast = {}
    inString = {}
    mustBeUnicode = {}
    mustTwoArguments = {}
    objectArgumentAfter = {}
    doesntDefineRound = {}
    mapIteration = {}
    keywordArguments = {}
    requiredArgumentNumber = {}
    doesNotIndexing = {}
    expectedOneArgument = {}
    canJoinIterable = {}
    mustBeStr = {}
    mustBeNoneStr = {}
    integerRequired = {}
    integerStartExpected = {}
    wantsInt = {}
    objectDontDeletion = {}
    doesTakeKeyword = {}
    gotUnexpectedKeyword = {}
    startswithFirstArg = {}
    mustStrNotInt = {}
    requiredArguments = {}

    def __init__(self, msg):
        self.msg = msg
        self.unsupportedOperand = {"unsupported operand":self.unsupportedOperandFunc()}
        self.objectNotIterable = {"object is not iterable":self.objectNotIterableFunc()}
        self.unorderableTypes = {"unorderable types":self.unorderableTypesFunc()}
        self.objectNoAttribute = {"object has no attribute":self.objectNoAttributeFunc()}
        self.notAllArgs = {"not all arguments converted during string formatting":self.notAllArgsFunc()}
        self.objectNotCallable = {"object is not callable":self.objectNotCallableFunc()}
        self.objectNotSubscriptable = {"object is not subscriptable":self.objectNotSubscriptableFunc()}
        self.cantMultiplyStr = {"can't multiply sequence by non-int of type":self.cantMultiplyStrFunc()}
        self.objectCannotInteger = {"object cannot be interpreted as an integer":self.objectCannotIntegerFunc()}
        self.argumentMustNumber = {"argument must be a string or a number":self.argumentMustNumberFunc()}
        self.objectToImplicitly = {"object to str implicitly":self.objectToImplicitlyFunc()}
        self.listMustIntegers = {"indices must be integers":self.listMustIntegersFunc()}
        self.hasNoLen = {"has no len()":self.hasNoLenFunc()}
        self.aBytesObjectNumber = {"a bytes-like object or a number":self.aBytesObjectNumberFunc()}
        self.cannotConcatenate = {"cannot concatenate":self.cannotConcatenateFunc()}
        self.integerArgsExpected = {"integer end argument expected":self.integerArgsExpectedFunc()}
        self.aFloatRequired = {"a float is required":self.aFloatRequiredFunc()}
        self.floatArgumentRequired = {"float argument required":self.floatArgumentRequiredFunc()}
        self.cantConvertComplex = {"can't convert complex to":self.cantConvertComplexFunc()}
        self.takesExactly = {"takes exactly":self.takesExactlyFunc()}
        self.formatANnumber = {"format: a number is required":self.formatANnumberFunc()}
        self.notFormatString = {"not enough arguments for format string":self.notFormatStringFunc()}
        self.canOnlyConcatenate = {"can only concatenate":self.canOnlyConcatenateFunc()}
        self.objectNotSupport = {"object does not support item assignment":self.objectNotSupportFunc()}
        self.requiredArgument = {"required positional argument:":self.requiredArgumentFunc()}
        self.invalidKeyword = {"is an invalid keyword argument for this function":self.invalidKeywordFunc()}
        self.sliceIndices = {"slice indices must":self.sliceIndicesFunc()}
        self.badUnary = {"bad operand type for unary":self.badUnaryFunc()}
        self.sequenceItem = {"sequence item":self.sequenceItemFunc()}
        self.takesMost = {"takes at most":self.takesMostFunc()}
        self.takesNoArguments = {"takes no arguments":self.takesNoArgumentsFunc()}
        self.takesLeastArgument = {"takes at least":self.takesLeastArgumentFunc()}
        self.argumentType = {"argument of type":self.argumentTypeFunc()}
        self.unhashableType = {"unhashable type":self.unhashableTypeFunc()}
        self.nonFormat = {"non-empty format":self.nonFormatFunc()}
        self.objectButReceived = {"object but received a":self.objectButReceivedFunc()}
        self.expectedBuffer = {"expected a character buffer":self.expectedBufferFunc()}
        self.expectedAtMost = {"expected at most":self.expectedAtMostFunc()}
        self.positionalArguments = {"positional arguments but":self.positionalArgumentsFunc()}
        self.cantConvertInt = {"can't convert non-string with explicit base":self.cantConvertIntFunc()}
        self.objectNeedsArgument = {"object needs an argument":self.objectNeedsArgumentFunc()}
        self.expectedAtLeast = {"expected at least":self.expectedAtLeastFunc()}
        self.inString = {"requires string as left operand":self.inStringFunc()}
        self.mustBeUnicode = {"must be unicode":self.mustBeUnicodeFunc()}
        self.mustTwoArguments = {"must have at least two arguments":self.mustTwoArgumentsFunc()}
        self.objectArgumentAfter = {"object argument after":self.objectArgumentAfterFunc()}
        self.doesntDefineRound = {"doesn't define":self.doesntDefineRoundFunc()}
        self.mapIteration = {"map() must support iteration":self.mapIterationFunc()}
        self.keywordArguments = {"takes no keyword arguments":self.keywordArgumentsFunc()}
        self.requiredArgumentNumber = {"Required argument":self.requiredArgumentNumberFunc()}
        self.doesNotIndexing = {"object does not support indexing":self.doesNotIndexingFunc()}
        self.expectedOneArgument = {"expected 1 arguments":self.expectedOneArgumentFunc()}
        self.canJoinIterable = {"can only join an iterable":self.canJoinIterableFunc()}
        self.mustBeStr = {"must be a string, bytes or code object":self.mustBeStrFunc()}
        self.mustBeNoneStr = {"must be None or a string":self.mustBeNoneStrFunc()}
        self.integerRequired = {"an integer is required":self.integerRequiredFunc()}
        self.integerStartExpected = {"integer start argument expected":self.integerStartExpectedFunc()}
        self.wantsInt = {"wants int":self.wantsIntFunc()}
        self.objectDontDeletion = {"object doesn't support item deletion":self.objectDontDeletionFunc()}
        self.doesTakeKeyword = {"does not take keyword arguments":self.doesTakeKeywordFunc()}
        self.gotUnexpectedKeyword = {"got an unexpected keyword":self.gotUnexpectedKeywordFunc()}
        self.startswithFirstArg = {"startswith first arg must be":self.startswithFirstArgFunc()}
        self.mustStrNotInt = {"must be str, not int":self.mustStrNotIntFunc()}
        self.requiredArguments = {"required positional arguments":self.requiredArgumentsFunc()}

        '''
        self. = {"":self.()}
        '''
        

    '''    Funções    '''
        
    def unsupportedOperandFunc(self):
        try:
            doisP = self.msg.split()[::-1]
            type1 = doisP[0]
            type2 = doisP[2]
            op = doisP[3].replace(":", "")            
            return """A operação """+op+""" não é suportada para os tipos """+type1+""" e """+type2+""". Verifique os tipos e suas operações."""
        except:
            return """"""
        
    
    def objectNotIterableFunc(self):
        try:
            typ = self.msg.split("'")[1]
            return """O objeto do tipo """+typ+""" não é iterável, é apenas uma literal, verifique se não é necessário o uso de uma lista ou o comando range()."""    
        except:
            return ""
    
    def unorderableTypesFunc(self):
        try:
            return """Os tipos não são comparáveis, por isso não é possível realizar a comparação: """+self.msg.split(":")[1]+""". Modifique-os para que sejam do mesmo tipo."""    
        except:
            return ""

    
    def objectNoAttributeFunc(self):
        try:
            typ = self.msg.split("'")
            type1 = typ[1]
            type2 = typ[3]
            message = ""
            if "getitem" in type2:
                message = """(não posso acessar item com o tipo """+type1+")." 
            return """O objeto do tipo """+type1+""" não tem nenhum atributo do tipo """+type2+""" """+message
        except:
            return ""

    
    def notAllArgsFunc(self):
        return """Nem todos os argumentos foram convertidos durante a formatação. Verifique a formatação, o uso do caractere %, os tipos das variáveis e argumentos."""    


    
    def objectNotCallableFunc(self):
        try:
            return self.msg.split("'")[1]+""" não é um objeto que possa ser invocado/chamado como uma função, verifique o uso dos () neste objeto. Para acessar um item use [ ], exemplo: [ item ]."""    
        except:
            return ""
    
    def objectNotSubscriptableFunc(self):
        try:
            return """O objeto do tipo """+self.msg.split("'")[1]+""" não pode ser acessado utilizando posição de memória através do uso de [], retire os colchetes."""    
        except:
            return ""
    

    def cantMultiplyStrFunc(self):
        try:
            return """Não é possível multiplicar uma sequência não numérica pelo tipo """+self.msg.split("'")[::-1][1]+""", corriga o problema convertendo para o tipo requerido, utilize o comando 'type'(). """    
        except:
            return ""
    
    
    def objectCannotIntegerFunc(self):
        try:
            return """O objeto do tipo """+self.msg.split("'")[1]+""" não pode ser interpretado como um inteiro, verifique os tipos para corrigir o problema."""
        except:
            return ""
    
    
    def argumentMustNumberFunc(self):
        try:
            return """A função"""+self.msg.split("(")[0]+"""() deve ter o argumento do tipo string ou número, não o tipo """+self.msg.split("'")[::-1][1]+"""."""
        except:
            return ""
    
    
    def objectToImplicitlyFunc(self):
        try:
            return """Não é possível converter o tipo """+self.msg.split("'")[2]+""" implicitamente para o tipo str, ou seja, por mais que seja compreensível sua conversão."""
        except:
            return ""
    
    
    def listMustIntegersFunc(self):
        try:
            return """Os índices de uma lista deve ser do tipo inteiro, não do tipo """+self.msg.split(",")[1].replace(" not ", "")
        except:
            return ""
        
    
    def hasNoLenFunc(self):
        try:
            return """O objeto do tipo """+self.msg.split("'")[1]+""" não tem tamanho, por isso não é possível utilizar a função len()."""
        except:
            return ""

    
    def aBytesObjectNumberFunc(self):
        try:
            return """O argumento da função"""+self.msg.split("(")[0]+"""() deve ser uma seqüência de caracteres ou bytes - como um objeto ou um número, não """+self.msg.split("'")[::-1][1] 
        except:
            return ""
    
    
    def cannotConcatenateFunc(self):
        try:
            t = self.msg.split("'")
            return """Não é possível concatenar os objetos do tipo """+t[1]+""" e """+t[3]
        except:
            return ""
    
    
    def integerArgsExpectedFunc(self):
        try:
            typ = self.msg.split(",")[1].replace(" got ","")
            return """O argumento do comando range() esperava que fosse um objeto do tipo inteiro, não do tipo """+typ
        except:
            return ""

    
    def aFloatRequiredFunc(self):
        return """O código esperava por um objeto do tipo float."""    

    
    def floatArgumentRequiredFunc(self):
        try:
            typ = self.msg.split(",")[1].replace(" not ", "")
            return """É necessário que o argumento seja do tipo float, não do tipo """+typ
        except:
            return ""

    
    def cantConvertComplexFunc(self):
        try:
            typ = self.msg.split(" ")[-1]
            return """Não é possível converter um número complexo para um número do tipo """+typ
        except:
            return ""

    
    def takesExactlyFunc(self):
        try:
            sep = self.msg.split("(")
            has = sep[-1].replace(" given)", "")
            func = sep[0]
            typ = self.msg.split(" ")[4]
            args = ""
            args = " argumento" if "1" in typ or "one" in typ else " argumentos"
            typ = "1" if typ=="one" else typ
            go = "foi passado " if "1" in has or "0" in has else "foram passados "  
            return """A função"""+func+"""() necessita de """+typ+args+""" e """+go+has
        except:
            return ""

    
    def formatANnumberFunc(self):
        try:
            typ = self.msg.split("not")[1]
            return """É necessário que o tipo a ser formatado seja um número, não o tipo"""+typ
        except:
            return ""

    
    def notFormatStringFunc(self):
        return """Os argumentos são insuficientes para formatar a string, verifique a quantidade de argumentos ou utilize parênteses para formatar em tuplas."""    

    
    def canOnlyConcatenateFunc(self):
        try:
            typ = self.msg.split("\"")[1]
            return """Não é possível concatenar o tipo """+typ+""" com uma lista, é necessário inserir este elemento, tente utilizar o comando append()."""
        except:
            return ""

    
    def objectNotSupportFunc(self):
        try:
            typ =  self.msg.split("'")[1]
            return """Ocorreu erro na atribuição, pois o objeto do tipo """+typ+""" não suporta a determinada atribuição, verifique se os tipos são iguais."""
        except:
            return ""

    
    def requiredArgumentFunc(self):
        try:
            spt = self.msg.split(" ")
            return """A função """+spt[1]+""" está faltando """+spt[3]+(" argumento" if spt[3] == "1" else " argumentos")+""" ou não foi instanciada corretamente. Verifique a quantidade de parâmetros."""
        except:
            return ""

    
    def invalidKeywordFunc(self):
        try:
            name = self.msg.split(" ")[1]
            return name+""" não é um nome válido para esta função. Verifique se não está usando uma palavra reservada ou algum comando ou variável de forma incorreta."""
        except:
            return ""

    
    def sliceIndicesFunc(self):
        return """Os índices para acessar um espaço de memória devem ser do tipo inteiro ou vazio caso queira criar um objeto vazio. Verifique se está colocando os índices de forma correta."""    

    
    def badUnaryFunc(self):
        try:
            name = self.msg.split(" ")[::-1]
            typ = name[0].replace("/n"," ").rstrip()
            op = name[1].replace(":", "")
            return """Não é possível realizar a operação unária """+op+""" no objeto do tipo """+typ+""", verifique o seu uso na expressão correspondente."""
        except:
            return ""

    
    def sequenceItemFunc(self):
        return """Esperava-se uma instância de uma string, mas outro tipo foi encontrado, verifique seus tipos."""  

    
    def takesMostFunc(self):
        try:
            name = self.msg.split(" ")
            func = name[1]
            X = name[5]
            Y = name[7].replace("(", "")
            return """A função """+func+""" possui no máximo """+X+(" argumento e " if X=="1" else " argumentos e ")+("foi passado " if Y=="1" else "foram passados ")+Y+""". Retire os argumentos em excesso para corrigir o erro."""
        except:
            return ""

    
    def takesNoArgumentsFunc(self):
        try:
            name = self.msg.split(" ")
            func = name[1]
            args = name[5].replace("(", "")
            return """A função """+func+""" não precisa de argumentos e """+("foi passado " if args=="1" else "foram passados ")+args+""". Remova os argumentos para corrigir o erro."""
        except:
            return ""

    
    def takesLeastArgumentFunc(self):
        try:
            name = self.msg.split(" ")
            func = name[1]
            X = name[5]
            Y = name[7].replace("(", "")
            return """A função """+func+""" precisa de pelo menos """+X+(" argumento " if X == "1" else " argumentos")+""" e """+("foi colocado " if Y=="1" or Y=="0" else " foram colocados ")+Y+"""."""
        except:
            return ""

    
    def argumentTypeFunc(self):
        try:
            typ = self.msg.split(" ")[4]
            return """O argumento do tipo """+typ+""" não é iterável, ou seja, não pode ser modificado adicionando outro valor ou não faz parte de um loop. Verifique se usou o comando if em vez do comando for para realizar um loop."""
        except:
            return ""

    
    def unhashableTypeFunc(self):
        return """Não é possível usar lista como chave de um dicionário, pois um dicionário precisa de chaves imutáveis. Verifique se o uso de uma tupla soluciona o problema. Exemplo: Isto é uma lista: [x, y] e isto é uma tupla: (x, y)."""    

    
    def nonFormatFunc(self):
        return """Não é possível formatar o objeto, verifique a declaração do comando format e seus parâmetros, por exemplo: format(valor, especificação) ou "string".format(especificação)."""    

    
    def objectButReceivedFunc(self):
        try:
            spt = self.msg.split("'")
            return """O comando """+spt[1]+""" necessita de um objeto do tipo """+spt[3]+""" mas recebeu um objeto do tipo """+spt[5]+""". Verifique os tipos de seus atributos."""
        except:
            return ""

    
    def expectedBufferFunc(self):
        return """Era esperado um parâmetro com uma sequência de caracteres, verifique os parâmetros dos comando utilizados. Tente converter os parâmetros para string - para isto utilize o comando: str(objeto)."""    

    
    def expectedAtMostFunc(self):
        try:
            name = self.msg.split(" ")
            command = name[1]
            X = name[5]
            Y = name[8]
            return """O comando """+command+""" possui no máximo """+X+(" argumento" if X == "1" or X =="0" else " argumentos")+""" e"""+(" foi colocado " if Y=="1" or Y=="0" else " foram colocados ")+Y.rstrip()+""". Verifique a quantidade de argumentos."""
        except:
            return ""

    
    def positionalArgumentsFunc(self):
        try:
            name = self.msg.split(" ")
            func = name[1]
            X = name[3]
            Y = name[7]
            return """A funçao """+func+""" precisa de """+X+(" argumento" if X == "1" or X =="0" else " argumentos")+""" e"""+(" foi passado " if Y=="1" or Y=="0" else " foram passados ")+Y.rstrip()+""". Verifique seus argumentos e declaração."""
        except:
            return ""

    
    def cantConvertIntFunc(self):
        return """A função int() não pode possuir mais que um parâmetro ou não pode converter o tipo de objeto. Verifique a quantidade de parâmetros e seus tipos."""    

    
    def objectNeedsArgumentFunc(self):
        try:
            name = self.msg.split(" ")
            return """O comando """+name[2]+""" do objeto do tipo """+name[4]+""" precisa de pelo menos um argumento."""
        except:
            return ""

    
    def expectedAtLeastFunc(self):
        return """O comando range precisa de pelo menos um argumento e não foi colocado nenhum."""    

    
    def inStringFunc(self):
        return """Só é possível utilizar o operador 'in' com objetos do tipo string, certifique que o objeto é do tipo string ou caractere: in <string>. Lembre-se que para percorrer uma lista, usa-se o comando de repetição 'for', não o comando condicional 'if'."""    

    
    def mustBeUnicodeFunc(self):
        return """O atributo deve ser do tipo unicode, não do tipo str ou int. Para obter uma strings unicode, use um prefixo u antes da string, exemplo: u'abc'."""    

    
    def mustTwoArgumentsFunc(self):
        try:
            name = self.msg.split(" ")[1]
            return """A função """+name+""" deve ter pelo menos dois argumentos."""
        except:
            return ""

    
    def objectArgumentAfterFunc(self):
        try:
            name = self.msg.split(" ")
            typ1 = name[1]
            typ2 = name[-1].rstrip()
            return """O objeto depois do argumento * deve ser do tipo """+typ1+""", não do tipo """+typ2+""". Verifique sua expressão."""
        except:
            return ""

    
    def doesntDefineRoundFunc(self):
        return """O método round() não pode ser utilizado com objetos do tipo str e tuple. Verifique o tipo do parâmetro."""    

    
    def mapIterationFunc(self):
        return """O método map() deve possuir argumentos que suportem iteração. Verifique os tipos dos argumentos."""    

    
    def keywordArgumentsFunc(self):
        try:
            func = self.msg.split(" ")[1]
            return """Os argumentos passados para a função """+func+""" não podem ser palavras chaves. Verifique os argumentos e seus tipos."""
        except:
            return ""


    def requiredArgumentNumberFunc(self):
        return """Não foi encontrado nenhum número como parâmetro para o comando utilizado. Verifique os argumentos e seus tipos ou o uso dos parênteses."""    

    
    def doesNotIndexingFunc(self):
        return """O objeto não suporta indexação, verifique o acesso aos índices deste objeto. """    

    
    def expectedOneArgumentFunc(self):
        try:
            func = self.msg.split(" ")[1]
            return """A função """+func+"""() esperava um argumento e não foi passado nenhum, verifique a quantidade de argumentos."""    
        except:
            return ""

    
    def canJoinIterableFunc(self):
        return """A função join() só pode ser usada em um objeto que pode ser iterável. Verifique os tipos dos objetos que está tentando unir."""    
    
    
    def mustBeStrFunc(self):
        try:
            func = self.msg.split(" ")[1]
            return """A função """+func+""" tem que possuir argumento do tipo string, byte ou objeto. Verifique os tipos dos argumentos."""
        except:
            return ""

    
    def mustBeNoneStrFunc(self):
        try:
            param = self.msg.split(" ")[1]
            return """O parâmetro """+param+""" deve vazio ou string, não o tipo inteiro, verifique os tipos dos parâmetros no código apresentado."""
        except:
            return ""

    
    def integerRequiredFunc(self):
        try:
            typ = self.msg.split("type")[1].replace(")", "")
            return """Foi esperado um objeto do tipo inteiro, porém foi obtido um objeto do tipo"""+typ+""". Verifique os tipos."""
        except:
            return ""

    
    def integerStartExpectedFunc(self):
        try:
            func = self.msg.split(" ")[1]
            typ = self.msg.split(", got")[1].rstrip()
            return """A função """+func+""" esperava um objeto do tipo inteiro e foi obtido um do tipo"""+typ
        except:
            return ""

    
    def wantsIntFunc(self):
        return """A operação com * requer que seja feita com dois ou mais números, verifique os tipos dos elementos e sua expressão."""    

    
    def objectDontDeletionFunc(self):
        try:
            typ = self.msg.split(" ")[1]
            return """Não é possível utilizar o comando del com objeto do tipo """+typ+"""."""
        except:
            return ""

    
    def doesTakeKeywordFunc(self):
        try:
            func = self.msg.split(" ")[1]
            return """A função """+func+""" foi usada com argumentos inválidos, verifique os tipos dos argumenos."""
        except:
            return ""

    
    def gotUnexpectedKeywordFunc(self):
        try:
            func = self.msg.split(" ")[1]
            return """Os argumentos da função """+func+""" não são válidos, verifique os seus tipos ou se realmente é uma expressão válida."""
        except:
            return ""

    
    def startswithFirstArgFunc(self):
        try:
            command = self.msg.split(" ")[1]
            return """O primeiro argumento do comando """+command+""" deve ser uma string, unicode ou uma tupla."""    
        except:
            return ""


    def mustStrNotIntFunc(self):
        return """O parâmetro deve ser do tipo string, não do tipo inteiro. Modifique os tipos dos parâmetros."""    

    
    def requiredArgumentsFunc(self):
        try:
            spt = self.msg.split(" ")
            func = spt[1]
            args = spt[3]
            typ1 = spt[7]
            typ2 = spt[9].rstrip()
            return """A função """+func+""" está faltando """+args+(" argumentos" if int(args)>1 else " argumento")+""", do tipo: """+typ1+""" e """+typ2+"""."""
        except:
            return ""
    
    '''
    
    def (self):
        return """ """    
    
    '''

    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.unsupportedOperand, self.objectNotIterable, self.unorderableTypes, self.objectNoAttribute, self.notAllArgs,
                         self.objectNotCallable, self.objectNotSubscriptable, self.cantMultiplyStr, self.objectCannotInteger, 
                         self.argumentMustNumber, self.objectToImplicitly, self.listMustIntegers, self.hasNoLen, self.aBytesObjectNumber,
                         self.cannotConcatenate, self.integerArgsExpected, self.aFloatRequired, self.floatArgumentRequired, self.cantConvertComplex,
                         self.takesExactly, self.formatANnumber, self.notFormatString, self.canOnlyConcatenate, self.objectNotSupport,
                         self.requiredArgument, self.invalidKeyword, self.sliceIndices, self.badUnary, self.sequenceItem, self.takesMost,
                         self.takesNoArguments, self.takesLeastArgument, self.argumentType, self.unhashableType, self.nonFormat, self.objectButReceived,
                         self.expectedBuffer, self.expectedAtMost, self.positionalArguments, self.cantConvertInt, self.objectNeedsArgument,
                         self.expectedAtLeast, self.inString, self.mustBeUnicode, self.mustTwoArguments, self.objectArgumentAfter,
                         self.doesntDefineRound, self.mapIteration, self.keywordArguments, self.requiredArgumentNumber, self.doesNotIndexing,
                         self.expectedOneArgument, self.canJoinIterable, self.mustBeStr, self.mustBeNoneStr, self.integerRequired,
                         self.integerStartExpected, self.wantsInt, self.objectDontDeletion, self.doesTakeKeyword, self.gotUnexpectedKeyword, self.startswithFirstArg,
                         self.mustStrNotInt, self.requiredArguments]}

    
