# -*- coding: utf-8 -*-

class Note(object):
    
    msg = ""
    dict = {}   
          
    
    def __init__(self, msg):
        self.msg = msg
        self.dict = {"each undeclared identifier is reported":self.undeclaredIdentifierFunc,
                     "’ declared here":self.varDeclaredHereFunc, "declared here":self.declaredHereFunc, 
                     "use option":self.useOptionFunc, "previous definition":self.previousDefinitionFunc, 
                     "previous declaration":self.previousDeclarationFunc, "expected":self.expectedTypeFunc, 
                     "expansion of macro":self.expansionOfMacroFunc, "originally":self.originallyFunc,
                     "previous implicit declaration":self.implicitDeclarationFunc, 
                     "an argument type that has":self.argumentTypeFunc,
                     "label":self.labelDefinedFunc, "ellipsis":self.ellipsisFunc,
                     "in definition of macro":self.definitionMacroFunc}
        
    '''
        self. = {"":self.()}
        '''  

    '''    Funções    '''
    
    def undeclaredIdentifierFunc(self):
        return """Cada identificador não declarado é reportado apenas uma vez para cada função em que ele aparece."""

    def varDeclaredHereFunc(self):
        try:
            line = self.msg.split(":")[1]
            var = self.msg.split("note:")[1]
            var = var.split("declared")[0]   
            return var+"""foi declarada no seguinte trecho de código na linha """+line+""":"""
        except:
            return ""
    
    def declaredHereFunc(self):
        try:
            return """Declarado no seguinte trecho de código na linha """+self.msg.split(":")[1] +""":"""
        except:
            return ""
             
    def useOptionFunc(self):
        return """Você também pode usar a opção -std=c99 ou -std=gnu99 para compilar o seu código.""" 
    
    def previousDefinitionFunc(self):
        try:
            line = self.msg.split(":")[1]
            var = self.msg.split("of")[1]
            var = var.split("was")[0]
            return """Definição prévia de"""+var+"""foi feita no seguinte trecho de código na linha """+line+""":"""
        except:
            return "fodeu"
    
    def previousDeclarationFunc(self):
        try:
            line = self.msg.split(":")[1]
            var = self.msg.split("of")[1]
            var = var.split("was")[0]
            return """Declaração prévia de"""+var+"""foi feita no seguinte trecho de código na linha """+line+""":"""
        except:
            return ""
        
    def expectedTypeFunc(self):
        try:
            type1 = self.msg.split("expected")[1]
            type1 = type1.split("but")[0]
            type2 = self.msg.split("type")[1]
            return """O tipo esperado é"""+type1+"""mas o argumento passado é do tipo"""+type2+"""."""
        except:
            return ""
        
    def expansionOfMacroFunc(self):
        try:
            return "Na expansão do macro"+self.msg.split("macro")[1]+""":"""
        except:
            return ""
    
    def originallyFunc(self):
        return "Originalmente definida no seguinte trecho de código:"
      
      
    def implicitDeclarationFunc(self):
        try:
            line = self.msg.split(":")[1]
            var = self.msg.split("of")[1]
            var = var.split("was")[0]
            return """Prévia declaração ímplicita de"""+var+"""feita no seguinte trecho de código na linha """+line+""":"""
        except:
            return ""       
    
    def argumentTypeFunc(self):
        return "Um tipo de argumento que tem uma promoção padrão não pode corresponder a uma declaração de lista de nomes de parâmetros vazios."    
    
    
    def labelDefinedFunc(self):
        try:
            line = self.msg.split(":")[1]
            label = self.msg.split("label")[1]
            label = label.split("defined")[0]
            return """Label"""+label+"""definida no seguinte trecho de código na linha """+line+""":"""
        except:
            return "" 
    
    def ellipsisFunc(self):
        return """"Lista de parâmetros errada."""     
             
             
    def definitionMacroFunc(self):
        try:
            return """Na definição do macro"""+self.msg.split("macro")[1]+"""."""
        except:
            return "" 
        
            
    def getNote(self, key):
        return self.dict[key]()
    
    
        