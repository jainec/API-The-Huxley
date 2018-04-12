# -*- coding: utf-8 -*-

class SyntaxE(object):

    msg = ""
    id = "SyntaxError"
    syntaxInvalid = {}
    missingPar = {}
    noAscii = {}
    unexpectedEOF = {}
    EOLwhileS = {}
    unexpectedChar = {}
    breakOutside = {}
    invalidToken ={}
    returnOutside = {}
    invalidChar= {}
    cantAssign = {}
    cantLiteral = {}
    cantOperator = {}
    EOFstring = {}
    nonKeyword = {}
    continueLoop = {}
    onlyExpression = {}
    EncodingProblem = {}
    cantComparison = {}
    keywordExpression = {}
    cantCall = {}
    codecByte = {}
    
    def __init__(self, msg):
        self.msg = msg
        self.syntaxInvalid = {"invalid syntax":self.syntaxInvalidFunc()}
        self.missingPar = {"Missing parentheses in call to":self.missingParFunc()}
        self.noAscii = {"Non-ASCII character":self.noAsciiFunc()}
        self.unexpectedEOF = {"unexpected EOF while parsing":self.unexpectedEOFFunc()}
        self.EOLwhileS = {"EOL while scanning string literal":self.EOLwhileSFunc()}
        self.unexpectedChar = {"unexpected character after line":self.unexpectedCharFunc()}
        self.breakOutside = {"'break' outside loop":self.breakOutsideFunc()}
        self.invalidToken = {"invalid token":self.invalidTokenFunc()}
        self.returnOutside = {"'return' outside function":self.returnOutsideFunc()}
        self.invalidChar = {"invalid character in identifier":self.invalidCharFunc()}
        self.cantAssign = {"can't assign to function call":self.cantAssignFunc()}
        self.cantLiteral = {"can't assign to literal":self.cantLiteralFunc()}
        self.cantOperator = {"can't assign to operator":self.cantOperatorFunc()}
        self.EOFstring = {"EOF while scanning triple-quoted string literal":self.EOFstringFunc()}
        self.nonKeyword = {"non-keyword arg after keyword arg":self.nonKeywordFunc()}
        self.continueLoop = {"'continue' not properly in loop":self.continueLoopFunc()}
        self.onlyExpression = {"only named arguments may follow *expression":self.onlyExpressionFunc()}
        self.EncodingProblem = {"encoding problem":self.EncodingProblemFunc()}
        self.cantComparison = {"can't assign to comparison":self.cantComparisonFunc()}
        self.keywordExpression = {"keyword can't be an expression":self.keywordExpressionFunc()}
        self.cantCall = {"can't delete function call":self.cantCallFunc()}
        self.codecByte = {"codec can't decode byte":self.codecByteFunc()}

        #self.var = {"chave":self.metodo()}

    '''    Funções    '''


    def syntaxInvalidFunc(self):
        return """Verifique se está faltando algum parênteses, a ausência de "":"" e declaração correta de alguns comandos, tais como: atribuição, if, for, while, input, print e outros."""


    def missingParFunc(self):
        return "Verifique o uso do parêntese, a partir da versão 3.0 do Python seu uso é obrigatório no comando print."

    
    def noAsciiFunc(self):
        return "Verifique o uso dos caracteres, especialmente os da língua portuguesa, visto que é diferente do padrão mundial. Insira o seguinte trecho do utf8 no início de seu programa: # -*- coding: utf-8 -*- . Mais informações em: www.python.org/peps/pep-0263.html."

   
    def unexpectedEOFFunc(self):
        return "Foram utilizados caracteres que não seguem o padrão da linguagem, assim ocorreu o erro de final de arquivo inesperado ao mostrar a saída. Verifique os caracteres utilizados ou a quantidade de parênteses ou aspas."
    
   
    def EOLwhileSFunc(self):
        return """EOL - End of line - o final de linha da declaração não foi fechado corretamente, insira " (aspas) em seu código para solucionar o problema e verifque se o número de aspas é par."""
    
   
    def unexpectedCharFunc(self):
        return "Foi inserido um caractere de forma errada no final da continuação da linha, verifque-o."
    
   
    def breakOutsideFunc(self):
        return """Foi identificado o mal uso do comando "break" fora de comandos de repetição. Verifique o seu uso ou identação."""
    
   
    def invalidTokenFunc(self):
        return """Foi feito o uso de forma errada do token. Geralmente o erro acontece ao usar a vírgula para representar números decimais ou usar o 0 antes de algum número, exemplo, respectivamente: 0,06 e 01."""
   
    def returnOutsideFunc(self):
        return """Foi feito o uso do comando return fora de uma função, retire-o ou verifique sua identação."""
    
   
    def invalidCharFunc(self):
        return """Foi feito o uso de um caractere inválido no contexto do código apresentado, verique os tipos e os caracteres."""
    
   
    def cantAssignFunc(self):
        return """Foi feita a chamada a alguma função de forma errada, verifique seu uso ou sua declaração."""
    
    
    def cantLiteralFunc(self):
        return """Foi feita a tentativa de atribuição a uma literal, isso não é possível, o comando de atribuição deve ser feito usando uma variável, por exemplo: variavel = expressão."""
   
    def cantOperatorFunc(self):
        return """Foi feita a tentativa de atribuição a um operador ou uma expressão de forma equivocada. Expressões devem ficar do lado direito do comando de atribuição."""
    
    def EOFstringFunc(self):
        return """Ocorreu um erro de final de arquivo durante o processamento da string no trecho do código, verifique o tamanho da string e se seus caracteres são do tipo strings."""
    
   
    def nonKeywordFunc(self):
        return """Não é possível colocar um argumento sem palavra-chave após um argumento que exige palavra-chave, verifique os argumentos e suas respectivas palavras chaves."""
    
   
    def continueLoopFunc(self):
        return """O "continue" foi usado de forma incorreta, normalmente é usado em comandos de repetição como: for e while."""
    
   
    def onlyExpressionFunc(self):
        return """Apenas argumentos nomeados podem seguir *expression. Tente utilizar parênteses e colocar os valores concatenados, exemplo: f(*(a+[3])) ou verificar o uso do sinal de multiplicação."""
    
   
    def EncodingProblemFunc(self):
        return """Ocorreu erro de codificação, verificar o padrão de codificação. Normalmente o mais utilizado é o padrão UTF8, ao inserir o comando: string.encode('utf8')."""
    
   
    def cantComparisonFunc(self):
        return """Não é possível realizar atribuição a uma comparação. Verifique o comando de atribuição."""
    
   
    def keywordExpressionFunc(self):
        return """Não é possível utilizar uma expressão como palavra chave,  tente utilizar " ou , ou + para separar as informações."""
    
   
    def cantCallFunc(self):
        return """Não é possível deletar a chamada de uma função, não sendo permitido o uso deste comando para tal."""
    
    def codecByteFunc(self):
        return """O arquivo está utilizando uma outra codificação, verique qual, a mais comum é o utf8 ou latin1."""
    
    
    '''def (self):
        return
    '''
   
    '''    Criação do dicionário    '''

    def getErros(self):
        return {self.id:[self.syntaxInvalid, self.missingPar, self.noAscii, self.unexpectedEOF, self.EOLwhileS, self.unexpectedChar, self.breakOutside,
                         self.invalidToken, self.returnOutside, self.invalidChar, self.cantAssign, self.cantLiteral, self.cantOperator, self.EOFstring,
                         self.nonKeyword, self.continueLoop, self.onlyExpression, self.EncodingProblem, self.cantComparison, self.keywordExpression,
                         self.cantCall, self.codecByte]}

