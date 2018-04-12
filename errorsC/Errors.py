# -*- coding: utf-8 -*-

class Error(object):

    msg = ""
    id = "error"
    calledObjectNotFunction = {}    
    tooFewArguments  = {}            
    tooManyArguments  = {}          
    staticFollowsNoStatic = {}      
    nestedFunction = {}             
    voidValueNotIgnored = {}        
    requireMoreArguments = {}       
    requireLessArgument = {}        
    invalideUseOfVoid  = {}         
    oldStyleDeclaration = {}        
    invalidStorageClass = {}        
    bracedGroup = {}                
    initializedAsVariable = {}      
    protypeDeclaration = {}         
    numberArgumentsDoesntMatch = {} 
    argumentDoesntMatchPrototype = {}
    undeclaredFirstUse = {}         
    declarationButNoParameter  = {} 
    redefinitionOfVariable  = {}    
    redeclarationOfVariable = {}    
    addressOfRegister = {}          
    undeclaredHere = {}             
    parameterIsInitialized = {}     
    redeclaredAsDifferentSymbol  = {}
    declaredVoid = {}               
    assignmentOfReadOnly = {}       
    decrementOfReadOnly = {}        
    incrementOfReadOnly = {}        
    unknownTypeName = {}            
    invalidOperandsToBinary  = {}   
    invalidTypeArgument  = {}       
    conflictingTypes = {}           
    incompatibleTypesAssigning = {} 
    incompatibleTypeArgument = {}   
    dereferencingPointer = {}       
    invalidTypeOfUnary = {}         
    typeFormalParameter  = {}       
    twoOrMoreDataTypes = {}         
    bothInDeclaration = {}          
    invalidUseOfUndefined = {}      
    invalidApplication = {}         
    conversionToNoScalar = {}       
    incompatibleTypesReturning = {} 
    fieldIncompleteType = {}        
    parameterIncompleteType = {}    
    fixedPointsTypes = {}           
    incompatibleTypesInitializing = {}
    expectedTokensAtEnd  = {}       
    expectedExpressionBefore  = {}  
    expectedDeclarationOrBefore = {}
    expectedIdentifierOrBefore = {} 
    expectedTokensBefore = {}      
    declarationStatementAtEnd = {}  
    expectedStatementBefore  = {}   
    expectedDeclarationBefore = {}  
    expectedToken1OrToken2 = {}     
    expectedIdentifierBefore = {}   
    expectedDeclarationOrAtEnd = {} 
    expectedTokenAtEnd = {}         
    expectedTokenIdentOrBefore = {} 
    expectedSpecifierQualifier = {} 
    expectedToken1BeforeToken2 = {} 
    strayInProgram = {}             
    elseWithoutIf  = {}             
    missingTerminatingChar  = {}    
    valueRequiredAsLeft = {}        
    storageClassSpecified = {}      
    breakNotWithinLoop = {}         
    invalidSuffix = {}     
    caseNotWithinSwitch = {}        
    initializerNotConstant  = {}    
    valueRequiredAsUnary = {}       
    valueRequiredAsIncrement = {}   
    emptyCharacterConstant = {}    
    invalidDigitInOctal = {}       
    caseNotReduceToInteger = {}    
    labelUsedButNotDefined = {}    
    forwardDeclaration = {}         
    tooManyDecimalPoints = {}       
    macroMustBeIdentifier = {}      
    switchQuantityNotInt = {}       
    defaultNotWithinSwitch = {}     
    exponentHasNoDigits = {}        
    unterminatedComment = {}        
    valueRequiredAsDecrement = {}   
    labelAtEndOfCompound = {}       
    labelCanOnlyBePartOfStatement = {}
    noFollowingHexDigits = {}       
    duplicateCaseValue = {}         
    previouslyUsedHere = {}         
    parameterNameOmitted = {}       
    continueNotWithinLoop = {}      
    duplicateLabel = {}             
    nearInitialization = {}         
    duplicateWord = {}              
    mayNotAppearInMacro = {}        
    duplicateMember = {}            
    jumpIntoScopeOfIdentifier = {}  
    subscriptNotInteger = {}        
    notAstructureOrUnion  = {}      
    neitherArrayNorPointer  = {}    
    hasNoMemberNamed = {}           
    arraySizeMissing = {}           
    incompleteElementType = {}      
    variableSizedObject = {}        
    sizeNoIntegerType = {}          
    invalidInitializer  = {}        
    modifiedAtFileScope = {}        
    flexibleArrayMember = {}        
    sizeTooLarge = {}               
    storageSizeNotKnown = {}        
    scalarIsRequired = {}               
    invalidPreprocessingDirective = {}
    includeExpects = {}             
    emptyFilename = {}              
    noMacroNameGiven = {}           
    loopInitialDeclarations = {}    
    tooLongForGCC = {}              

    def __init__(self, msg):
        self.msg = msg
        self.calledObjectNotFunction = {"is not a function or function pointer":self.calledObjectNotFunctionFunc()}
        self.tooFewArguments = {"too few arguments to function":self.tooFewArgumentsFunc()}
        self.tooManyArguments = {"too many arguments to function":self.tooManyArgumentsFunc()}
        self.staticFollowsNoStatic = {"follows non-static declaration":self.staticFollowsNoStaticFunc()}
        self.nestedFunction = {"nested function":self.nestedFunctionFunc()}
        self.voidValueNotIgnored = {"void value not ignored":self.voidValueNotIgnoredFunc()}
        self.requireMoreArguments = {"arguments, but only":self.requireMoreArgumentsFunc()}
        self.requireLessArgument = {"arguments, but takes just":self.requireLessArgumentFunc()}
        self.invalideUseOfVoid = {"invalid use of void expression":self.invalideUseOfVoidFunc()}
        self.oldStyleDeclaration = {"old-style parameter":self.oldStyleDeclarationFunc()}
        self.invalidStorageClass = {"invalid storage class for function":self.invalidStorageClassFunc()}
        self.bracedGroup = {"braced-group within expression":self.bracedGroupFunc()}
        self.initializedAsVariable = {"is initialized like a variable":self.initializedAsVariableFunc()}
        self.protypeDeclaration = {"prototype declaration":self.protypeDeclarationFunc()}
        self.numberArgumentsDoesntMatch = {"number of arguments doesn’t match":self.numberArgumentsDoesntMatchFunc()}
        self.argumentDoesntMatchPrototype = {"’ doesn’t match prototype":self.argumentDoesntMatchPrototypeFunc()}
        self.undeclaredFirstUse = {"undeclared (first use in this function)":self.undeclaredFirstUseFunc()}
        self.declarationButNoParameter = {"but no such parameter":self.declarationButNoParameterFunc()}
        self.redefinitionOfVariable = {"redefinition of":self.redefinitionOfVariableFunc()}
        self.redeclarationOfVariable = {"with no linkage":self.redeclarationOfVariableFunc()}
        self.addressOfRegister = {"address of register variable":self.addressOfRegisterFunc()}
        self.undeclaredHere = {"undeclared here (not in a function)":self.undeclaredHereFunc()}
        self.parameterIsInitialized = {"is initialized":self.parameterIsInitializedFunc()}
        self.redeclaredAsDifferentSymbol = {"different kind of symbol":self.redeclaredAsDifferentSymbolFunc()}
        self.declaredVoid = {"variable or field":self.declaredVoidFunc()}
        self.assignmentOfReadOnly = {"assignment of read-only variable":self.assignmentOfReadOnlyFunc()}
        self.decrementOfReadOnly = {"decrement of read-only variable":self.decrementOfReadOnlyFunc()}
        self.incrementOfReadOnly = {"increment of read-only variable":self.incrementOfReadOnlyFunc()}
        self.unknownTypeName = {"unknown type name":self.unknownTypeNameFunc()}
        self.invalidOperandsToBinary = {"invalid operands to binary":self.invalidOperandsToBinaryFunc()}
        self.invalidTypeArgument = {"invalid type argument of ‘->’":self.invalidTypeArgumentFunc()}
        self.conflictingTypes = {"conflicting types for":self.conflictingTypesFunc()}
        self.incompatibleTypesAssigning = {"incompatible types when assigning":self.incompatibleTypesAssigningFunc()}
        self.incompatibleTypeArgument = {"incompatible type for argument":self.incompatibleTypeArgumentFunc()}
        self.dereferencingPointer = {"dereferencing pointer to incomplete":self.dereferencingPointerFunc()}
        self.invalidTypeOfUnary = {"invalid type argument of unary":self.invalidTypeOfUnaryFunc()}
        self.typeFormalParameter = {"type of formal parameter":self.typeFormalParameterFunc()}
        self.twoOrMoreDataTypes = {"two or more data types":self.twoOrMoreDataTypesFunc()}
        self.bothInDeclaration = {"both":self.bothInDeclarationFunc()}
        self.invalidUseOfUndefined = {"invalid use of undefined type":self.invalidUseOfUndefinedFunc()}
        self.invalidApplication = {"invalid application of":self.invalidApplicationFunc()}
        self.conversionToNoScalar = {"conversion to non-scalar type":self.conversionToNoScalarFunc()}
        self.incompatibleTypesReturning = {"returning type":self.incompatibleTypesReturningFunc()}
        self.fieldIncompleteType = {"field ‘":self.fieldIncompleteTypeFunc()}
        self.parameterIncompleteType = {"has incomplete type":self.parameterIncompleteTypeFunc()}
        self.fixedPointsTypes = {"fixed-point types":self.fixedPointsTypesFunc()}
        self.incompatibleTypesInitializing = {"when initializing":self.incompatibleTypesInitializingFunc()}      
        self.expectedTokensAtEnd = {"expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ at end of input":self.expectedTokensAtEndFunc()}
        self.expectedExpressionBefore = {"expected expression before":self.expectedExpressionBeforeFunc()}
        self.expectedDeclarationOrBefore = {"expected declaration specifiers or":self.expectedDeclarationOrBeforeFunc()}
        self.expectedIdentifierOrBefore = {"expected identifier or":self.expectedIdentifierOrBeforeFunc()}
        self.expectedTokensBefore = {"expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before":self.expectedTokensBeforeFunc()}
        self.declarationStatementAtEnd = {"expected declaration or statement at end of input":self.declarationStatementAtEndFunc()}
        self.expectedStatementBefore = {"expected statement before":self.expectedStatementBeforeFunc()}
        self.expectedDeclarationBefore = {"expected declaration specifiers before":self.expectedDeclarationBeforeFunc()}
        self.expectedToken1OrToken2 = {"’ or ‘":self.expectedToken1OrToken2Func()}
        self.expectedIdentifierBefore = {"expected identifier before":self.expectedIdentifierBeforeFunc()}
        self.expectedDeclarationOrAtEnd = {"expected declaration specifiers or ‘...’ at end of input":self.expectedDeclarationOrAtEndFunc()}
        self.expectedTokenAtEnd = {"at end of input":self.expectedTokenAtEndFunc()}
        self.expectedTokenIdentOrBefore = {", identifier or":self.expectedTokenIdentOrBeforeFunc()}
        self.expectedSpecifierQualifier = {"expected specifier-qualifier-list before":self.expectedSpecifierQualifierFunc()}
        self.expectedToken1BeforeToken2 = {"expected":self.expectedToken1BeforeToken2Func()}
        self.strayInProgram = {"stray":self.strayInProgramFunc()}
        self.elseWithoutIf = {"without a previous":self.elseWithoutIfFunc()}
        self.missingTerminatingChar = {"missing terminating":self.missingTerminatingCharFunc()}
        self.valueRequiredAsLeft = {"lvalue required as left operand of assignment":self.valueRequiredAsLeftFunc()}
        self.storageClassSpecified = {"storage class specified for parameter":self.storageClassSpecifiedFunc()}
        self.breakNotWithinLoop = {"break statement not within loop or switch":self.breakNotWithinLoopFunc()}
        self.invalidSuffix = {"invalid suffix":self.invalidSuffixFunc()}
        self.caseNotWithinSwitch = {"case label not within a switch statement":self.caseNotWithinSwitchFunc()}
        self.initializerNotConstant = {"initializer element is not constant":self.initializerNotConstantFunc()}
        self.valueRequiredAsUnary = {"lvalue required as unary":self.valueRequiredAsUnaryFunc()}
        self.valueRequiredAsIncrement = {"lvalue required as increment operand":self.valueRequiredAsIncrementFunc()}
        self.emptyCharacterConstant = {"empty character constant":self.emptyCharacterConstantFunc()}
        self.invalidDigitInOctal = {"in octal constant":self.invalidDigitInOctalFunc()}
        self.caseNotReduceToInteger = {"not reduce to an integer constant":self.caseNotReduceToIntegerFunc()}
        self.labelUsedButNotDefined = {"used but not defined":self.labelUsedButNotDefinedFunc()}
        self.forwardDeclaration = {"has just a forward declaration":self.forwardDeclarationFunc()}
        self.tooManyDecimalPoints = {"too many decimal points in number":self.tooManyDecimalPointsFunc()}
        self.macroMustBeIdentifier = {"macro names must be identifiers":self.macroMustBeIdentifierFunc()}
        self.switchQuantityNotInt = {"switch quantity not an integer":self.switchQuantityNotIntFunc()}
        self.defaultNotWithinSwitch = {"‘default’ label not within a switch statement":self.defaultNotWithinSwitchFunc()}
        self.exponentHasNoDigits = {"exponent has no digits":self.exponentHasNoDigitsFunc()}
        self.unterminatedComment = {"unterminated comment":self.unterminatedCommentFunc()}
        self.valueRequiredAsDecrement = {"lvalue required as decrement operand":self.valueRequiredAsDecrementFunc()}
        self.labelAtEndOfCompound = {"label at end of compound statement":self.labelAtEndOfCompoundFunc()}
        self.labelCanOnlyBePartOfStatement = {"a label can only be part of a statement":self.labelCanOnlyBePartOfStatementFunc()}
        self.noFollowingHexDigits = {"\\x used with no following hex digits":self.noFollowingHexDigitsFunc()}
        self.duplicateCaseValue = {"duplicate case value":self.duplicateCaseValueFunc()}
        self.previouslyUsedHere = {"previously used here":self.previouslyUsedHereFunc()}
        self.parameterNameOmitted = {"parameter name omitted":self.parameterNameOmittedFunc()}
        self.continueNotWithinLoop = {"continue statement not within a loop":self.continueNotWithinLoopFunc()}
        self.duplicateLabel = {"duplicate label":self.duplicateLabelFunc()}
        self.nearInitialization = {"near initialization for":self.nearInitializationFunc()}
        self.duplicateWord = {"duplicate ‘":self.duplicateWordFunc()}
        self.mayNotAppearInMacro = {"may not appear in macro parameter list":self.mayNotAppearInMacroFunc()}
        self.duplicateMember = {"duplicate member":self.duplicateMemberFunc()}
        self.jumpIntoScopeOfIdentifier = {"jump into scope of identifier":self.jumpIntoScopeOfIdentifierFunc()}
        self.subscriptNotInteger = {"array subscript is not an integer":self.subscriptNotIntegerFunc()}
        self.notAstructureOrUnion = {"in something not a structure or union":self.notAstructureOrUnionFunc()}
        self.neitherArrayNorPointer = {"subscripted value is neither array":self.neitherArrayNorPointerFunc()}
        self.hasNoMemberNamed = {"has no member named":self.hasNoMemberNamedFunc()}
        self.arraySizeMissing = {"array size missing in":self.arraySizeMissingFunc()}
        self.incompleteElementType = {"array type has incomplete element type":self.incompleteElementTypeFunc()}
        self.variableSizedObject = {"variable-sized object":self.variableSizedObjectFunc()}
        self.sizeNoIntegerType = {"has non-integer type":self.sizeNoIntegerTypeFunc()}
        self.invalidInitializer = {"invalid initializer":self.invalidInitializerFunc()}
        self.modifiedAtFileScope = {"at file scope":self.modifiedAtFileScopeFunc()}
        self.flexibleArrayMember = {"flexible array member":self.flexibleArrayMemberFunc()}
        self.sizeTooLarge = {"is too large":self.sizeTooLargeFunc()}
        self.storageSizeNotKnown = {"storage size":self.storageSizeNotKnownFunc()}
        self.scalarIsRequired = {"where scalar is required":self.scalarIsRequiredFunc()}    
        self.invalidPreprocessingDirective = {"invalid preprocessing directive":self.invalidPreprocessingDirectiveFunc()}
        self.includeExpects = {"include expects":self.includeExpectsFunc()}
        self.emptyFilename = {"empty filename in":self.emptyFilenameFunc()}
        self.noMacroNameGiven = {"no macro name given in":self.noMacroNameGivenFunc()}
        self.loopInitialDeclarations = {"loop initial declarations":self.loopInitialDeclarationsFunc()}
        self.tooLongForGCC = {"is too long for GCC":self.tooLongForGCCFunc()}
        
        '''
        self. = {"":self.()}
        '''
        

    '''    Funções    '''
        
    def calledObjectNotFunctionFunc(self):
        try:
            objeto = self.msg.split(" ")[2]
            if objeto == "is":
                objeto = ""         
            return """O objeto """+objeto+""" chamado não é uma função nem um ponteiro para uma função, mas você está o chamando como se fosse, pois está passando argumentos como parâmetros entre parênteses (). Certifique-se de não passar argumentos para uma variável, e se """+objeto+""" for um vetor, certifique-se de estar usando colchetes [] ao invés de parênteses () para acessar suas posições."""
        except:
            return ""
        
    
    def tooFewArgumentsFunc(self):
        try:
            return """Poucos argumentos na função"""+self.msg.split("function")[1]+""". Na chamada da função você está passando menos argumentos do que a função requer. Verifique quantos argumentos a função recebe na sua declaração e certifique-se de passar o mesmo número de argumentos sempre que chamá-la."""    
        except:
            return ""
    
    
    def tooManyArgumentsFunc(self):
        try:
            return """Muitos argumentos na função"""+self.msg.split("function")[1]+""". Na chamada da função vocẽ está passando mais argumentos do que a função espera. Verifique quantos argumentos a função recebe na sua declaração e certifique-se de passar o mesmo número de argumentos sempre que chamá-la."""    
        except:
            return ""

    
    def staticFollowsNoStaticFunc(self):
        try:
            function = self.msg.split("of")[1]
            funcao = function.split("follows")[0]
            return """Lembre-se de que em C uma variável 'static' declarada dentro de uma função mantém seu valor entre chamadas dessa função, mas se a variável 'static' for global, então ela é "vista" apenas no arquivo onde ela foi declarada. Assim, se você gostaria de usar"""+funcao+"""fora de onde ela foi declarada, remova a palavra 'static' de sua declaração."""
        except:
            return ""

    
    def nestedFunctionFunc(self):
        return """Lembre-se de que C não suporta funções aninhadas (nested functions). Defina-as de forma não aninhada para corrigir o problema."""    


    
    def voidValueNotIgnoredFunc(self):
        try:
            return """Valor 'void' não está sendo respeitado como deveria. Você está tentando fazer uma comparação ou atribuição com o retorno de uma função que foi declarada como 'void', e logo, não retorna nenhum valor. Se você quer que a função retorne algum valor não a declare com retorno do tipo void mas sim com o tipo que você deseja retornar (int, double, char...) e no final dela use 'return' para retornar o valor que você deseja."""    
        except:
            return ""
    
    def requireMoreArgumentsFunc(self):
        try:
            function = self.msg.split("requires")[0]
            funcao = function.split("macro")[1].strip(" ")
            numbers = self.msg.split(" ")
            num1 = numbers[3]
            num2 = numbers[7]
            return funcao+""" requer """+num1+""" argumentos como parâmetros, mas só foram dados """+num2+"""."""
        except:
            return ""
    

    def requireLessArgumentFunc(self):
        try:
            function = self.msg.split("passed")[0]
            funcao = function.split("macro")[1]
            numbers = self.msg.split(" ")
            num1 = numbers[3]
            num2 = numbers[8]
            return """Foram passados """+num1+""" argumentos para"""+funcao+""", mas a função pode receber apenas """+num2+"""."""
        except:
            return ""
    
    
    def invalideUseOfVoidFunc(self):
        try:
            return """Você está tentando fazer uso do valor de retorno de uma função que foi declarada como 'void', e logo, não retorna nenhum valor. Se você quer que a função retorne algum valor não a declare como 'void', mas sim como o tipo que você deseja retornar (int, double, char...) e no final dela use 'return' para retornar o valor que você deseja."""
        except:
            return ""
    
    
    def oldStyleDeclarationFunc(self):
            return """Você está utilizando um estilo antigo de declaração de funções em C. Para corrigir esse erro, coloque todo o escopo da função, incluindo as declarações de variáveis, dentro de chaves "{ }", exemplo: void funcao(int n){ todo o código da função }."""
    
    
    def invalidStorageClassFunc(self):
            return """Esse tipo de erro é um erro de cabeçalho (header) e ele geralmente ocorre ao declarar uma função 'static' dentro de outra. Certifique-se de não fazer isso."""
    
    
    def bracedGroupFunc(self):
            return """Tipo de expressão inválida. Tente retirar os parênteses para corrigir o erro."""
        
    
    def initializedAsVariableFunc(self):
        try:
            function = self.msg.split("function")[1]
            funcao = function.split("is")[0]
            return """A função"""+funcao+"""foi inicializada como uma variável. Em C funções não podem ser inicializadas de forma análoga às variáveis. Certifique-se de definir a função corretamente. Se"""+funcao+"""for um vetor, certifique-se de estar usando colchetes [] e não parênteses () junto ao seu nome."""
        except:
            return ""
        
        
    def protypeDeclarationFunc(self):
        return """Verifique a declaração do protótipo da função para descobrir a quantidade e os tipos de argumentos que ela recebe."""
        
        
    def numberArgumentsDoesntMatchFunc(self):
        try:
            return """O número de argumentos passados como parâmetro da função não está de acordo com o número de argumentos definidos no protótipo da função. Verifique o protótipo da função e certifique-se de passar o mesmo número de argumentos sempre que chamá-la."""
        except:
            return ""
                
        
    def argumentDoesntMatchPrototypeFunc(self):
        try:
            argument = self.msg.split("argument")[1]
            arg = argument.split("doesn’t")[0]
            return """O argumento"""+arg+"""passado não está de acordo com o protótipo da função em questão. Verifique o protótipo da função e certifique-se de passar a quantidade e os tipos de argumentos que ela recebe corretamente."""
        except:
            return ""
            
    def undeclaredFirstUseFunc(self):
        try:
            var = self.msg.split("undeclared")[0]         
            return """A variável """+var+"""não foi declarada antes de ser usada. Lembre-se de que na linguagem C todas as variáveis têm que ser declaradas antes de serem usadas. Certifique-se de declarar """+var+"""listando seu tipo e nome."""
        except:
            return ""
        
    
    def declarationButNoParameterFunc(self):
        try:
            variavel = self.msg.split("parameter")[1]
            var = variavel.split("but")[0]
            return """A declaração da variável"""+var+"""apresenta problemas pois você não está demarcando o escopo da função principal (main) corretamente. Lembre-se de que em C o código executado deve estar dentro da função main, e o escopo dessa função deve ser demarcado com chaves "{}", por exemplo: int main() { código }. Portanto, coloque as chaves para corrigir o erro."""    
        except:
            return ""
    
    
    def redefinitionOfVariableFunc(self):
        try:
            return """Você está declarando a variável"""+self.msg.split("of")[1]+""" mais de uma vez no mesmo escopo. Certifique-se de definir cada variável apenas uma vez por escopo."""    
        except:
            return ""

    
    def redeclarationOfVariableFunc(self):
        try:
            variavel = self.msg.split("of")[1]
            var = variavel.split("with")[0]
            return """Declaração da variável"""+var+"""mais de uma vez no mesmo escopo. Lembre-se: na linguagem C não é permitido declarar duas ou mais variáveis com o mesmo nome no mesmo escopo. Tente atribuir nomes diferentes às variáveis."""
        except:
            return ""

        
    def addressOfRegisterFunc(self):
        try:
            variavel = self.msg.split("variable")[1]
            var = variavel.split("requested")[0]
            return """Você declarou a variável"""+var+"""como "register", logo, ela é armazenada em um registrador e não na memória. Assim, o erro está acontecendo porque você está tentando acessar o endereço dessa variável na memória. Para corrigir esse erro da forma mais fácil, retire a palavra-chave "register" da declaração da variável e trabalhe com ela normalmente, ou se preferir mantê-la como um "register" não utilize operadores de memória com ela, como o "&"."""
        except:
            return ""    

    
    def undeclaredHereFunc(self):
        try:
            var = self.msg.split("undeclared")[0]    
            return """A variável """+var+"""não foi declarada antes de ser usada. Lembre-se de que na linguagem C todas as variáveis têm que ser declaradas antes de serem usadas. Certifique-se de declarar """+var+"""listando seu tipo e nome."""
        except:
            return ""
    

    def parameterIsInitializedFunc(self):
        try:
            variavel = self.msg.split("parameter")[1]
            var = variavel.split("is")[0]
            return """A inicialização da variável"""+var+"""apresenta problemas pois você não está demarcando o escopo da função principal (main) corretamente. Lembre-se de que em C o código executado deve estar dentro da função main, e o escopo dessa deve ser demarcado com chaves "{}", por exemplo: int main() { código }. Portanto, coloque as chaves para corrigir o erro."""    
        except:
            return ""
    
    
    def redeclaredAsDifferentSymbolFunc(self):
        try:
            var = self.msg.split("redeclared")[0]
            return """A variável """+var+"""é um parâmetro da função. Logo, não precisa ser redeclarada dentro dela, ou seja, não é mais necessário listar o tipo de """+var+"""antes de usá-la na função."""
        except:
            return ""
    
    
    def declaredVoidFunc(self):
        try:
            variavel = self.msg.split("field")[1]
            var = variavel.split("declared")[0]
            return """Variável"""+var+"""declarada 'void'. Na linguagem C não se pode declarar uma variável do tipo 'void'. Tente usar algum tipo possível como int, char, float, double ou outro."""
        except:
            return ""
    
    
    def assignmentOfReadOnlyFunc(self):
        try:
            return """Atribuição a uma variável que foi declarada como constante. Lembre-se de que não é permitido modificar (atribuir, incrementar, decrementar) valores de constantes em C. Para essas variáveis só é possível ler o valor, mas não modificá-lo. Se quiser modificar o valor da variável"""+self.msg.split("variable")[1]+""", retire a palavra 'const' da sua declaração."""
        except:
            return ""
    
    
    def decrementOfReadOnlyFunc(self):
        try:
            return """Decremento de uma variável que foi declarada como constante. Lembre-se de que não é permitido modificar (atribuir, incrementar, decrementar) valores de constantes em C. Para essas variáveis só é possível ler o valor, mas não modificá-lo. Se quiser modificar o valor de"""+self.msg.split("variable")[1]+""", retire a palavra 'const' da sua declaração, o que fará com que passe a ser uma variável, podendo portanto mudar de valor."""
        except:
            return ""
        
    
    def incrementOfReadOnlyFunc(self):
        try:
            return """Incremento de uma variável que foi declarada como constante. Lembre-se de que não é permitido modificar (atribuir, incrementar, decrementar) valores de constantes em C. Para essas variáveis só é possível ler o valor, mas não modificá-lo. Se quiser modificar o valor da variável"""+self.msg.split("variable")[1]+""", retire a palavra 'const' da sua declaração."""
        except:
            return ""
        
        
    def unknownTypeNameFunc(self):
        try:
            name = self.msg.split("name")[1]           
            return """O tipo"""+name+""" é desconhecido em C. Certifique-se de usar tipos existentes na linguagem C como: int, float, char, double, entrou outros, ou tipos definidos por você corretamente utilizando o 'typedef'."""
        except:
            return """"""
        
    
    def invalidOperandsToBinaryFunc(self):
        try:
            operand = self.msg.split("binary")[1]
            op = operand.split("(")[0].replace(" ","")
            typ = self.msg.split("have")[1]
            type1 = typ.split("and")[0]
            type2 = typ.split("and")[1].replace(")", "")
            return """Tipos de operandos inválidos para o operador binário """+op+""". Você está usando os tipos"""+type1+"""e"""+type2+""" com o operador """+op+""", o que não é correto. Para corrigir o erro tente utilizar operadores binários com duas variáveis do tipo 'int'. Obs: Na maioria dos casos que esse erro ocorre com o operador '&' é porque o usuário esquece alguma(s) ',' (vírgula(s)). Verifique-as."""    
        except:
            return ""
    
    
    def invalidTypeArgumentFunc(self):
        try:
            typ = self.msg.split("have")[1].replace(")", "")
            typ = typ.replace(")", "")
            return """O argumento do lado esquerdo do '->' deve ser um ponteiro."""+typ+""" não é um ponteiro, logo você deve usar o operador ponto '.' ao ínves do '->' para acessar um membro de"""+typ+""". Por exemplo: reg[i].campo ao ínves de reg[i]->campo."""    
        except:
            return ""

    
    def conflictingTypesFunc(self):
        try:
            name = self.msg.split("for ")[1]
            return """Conflito de tipos com """+name+""". Se """+name+""" for uma variável, então você está declarando variáveis com o mesmo nome mas com tipos diferentes. Certifique-se de atribuir nomes diferentes às variáveis. Se """+name+""" for uma função, certifique-se de defini-la antes de usá-la no código e de usar a mesma quantidade e os mesmos tipos de argumentos tanto na definição quanto na chamada para o uso da mesma."""
        except:
            return ""

    
    def incompatibleTypesAssigningFunc(self):
        try:
            typ = self.msg.split("type ")
            type1 = typ[1].replace("from", "").strip(" ")
            type2 = typ[2]
            return """Tipos incompatíveis para atribuição. Você está atribuindo o tipo """+type2+""" para um objeto do tipo """+type1+""". Certifique-se de fazer atribuições entre variáveis de tipos iguais."""
        except:
            return ""    

    
    def incompatibleTypeArgumentFunc(self):
        try:
            function = self.msg.split("of")[1]
            numero = self.msg.split("argument")[1]
            number = numero.split("of")[0]
            return """Tipo incompatível do argumento"""+number+"""da função"""+function+""". Certifique-se de passar como parâmetro na chamada de """+function+""" os mesmos tipos de argumentos especificados na sua definição."""    
        except:
            return ""
        
    
    def dereferencingPointerFunc(self):
        return """Você está tentando referenciar um campo de um registro/struct que foi declarado de forma errada no código. Se você declarou o registro/struct usando 'typedef', então certifique-se de omitir a palavra-chave 'struct' da declaração de registros desse tipo para corrigir o erro. Mas se você estiver usando mais de um arquivo .c, então utilize apenas um e coloque todas as definições nele."""    
    

    def invalidTypeOfUnaryFunc(self):
        try:
            typ = self.msg.split("have")[1].replace(")", "")
            return """Tipo de argumento inválido para o operador unário '*'. Nesse caso, você está usando o '*' para tentar obter o endereço de uma variável do tipo"""+typ+""", mas esse tipo não é um ponteiro e logo isso não é permitido. Remova o operador '*' para corrigir o erro. Se você estiver tentando usar o '*' para realizar uma multiplicação, tente colocar parênteses corretamente para separar os termos."""    
        except:
            return ""
    
    
    def typeFormalParameterFunc(self):
        try:
            numero = self.msg.split("parameter")[1]
            number = numero.split("is")[0]
            return """O tipo do parâmetro de número"""+number+"""que você está passando para a função em questão é diferente do tipo esperado que foi definido na declaração da função. Certifique-se de passar como argumento na posição"""+number+"""um parâmetro do tipo esperado."""
        except:
            return ""
    
    
    def twoOrMoreDataTypesFunc(self):
        return """Você está declarando um especificador com dois ou mais tipos. Certifique-se de usar apenas um tipo de dado (int, char, float, double, entre outros) nas declarações de especificadores."""
    
    
    def bothInDeclarationFunc(self):
        try:
            typ = self.msg.split("both")[1]
            type1 = typ.split("and")[0]
            typ = self.msg.split("and")[1]
            type2 = typ.split("in")[0]
            return """Em C não é permitido usar"""+type1+"""e"""+type2+"""juntos para declarar variáveis. Para corrigir o erro retire o"""+type1+"""da declaração e lembre-se de que os tipos primitivos para declarar variáveis em C são: char, unsigned char, int, unsigned int, short int, unsigned short int, long int, unsigned long int, float, double e long double."""
        except:
            return ""
    
    
    def invalidUseOfUndefinedFunc(self):
        try:
            typ = self.msg.split("type")[1]
            return """Tipo"""+typ+""" não reconhecido. Esse erro geralmente acontece quando o programador utiliza mais de um arquivo .c no seu código. Assim, a definição de uma estrutura que está em um arquivo .c não é reconhecida por outro. Para corrigir o erro da forma mais simples utilize apenas um arquivo.c e coloque todas as definições nele, caso contrário, inclua a definição de"""+typ+""" no arquivo .h (cabeçalho (header)) correspondente e inclua esse .h (#include "arquivo.h") em todos os programas .c que utilizarem esse tipo."""
        except:
            return ""
        
        
    def invalidApplicationFunc(self):
        try:
            typ = self.msg.split("type")[1]
            return """Aplicação inválida do 'sizeof' ao tipo"""+typ+""". Esse erro geralmente acontece quando o programador utiliza mais de um arquivo .c no seu código. Assim, a definição de uma estrutura que está em um arquivo.c não é reconhecida por outro .c. Para corrigir o erro da forma mais simples utilize apenas um arquivo.c e coloque todas as definições nele, caso contrário inclua a definição de"""+typ+""" no arquivo .h (cabeçalho (header)) correspondente e inclua esse .h (#include "arquivo.h") em todos os programas .c que utilizarem esse tipo."""
        except:
            return ""
        
        
    def conversionToNoScalarFunc(self):
        return """Conversão inválida na alocação. Para corrigir esse erro, tente colocar o '*' dentro dos parênteses que vêm antes do malloc/realloc/calloc. Exemplo: estrutura = (tipo*) malloc(...) ao invés de estrutura = (tipo) malloc(...)."""
        
        
    def incompatibleTypesReturningFunc(self):
        try:
            typ = self.msg.split("type")[2]
            type1 = typ.split("but")[0]
            type2 = typ.split("but")[1].replace("was expected", "")
            return """O tipo"""+type1+"""está sendo retornado quando o tipo"""+type2+"""é esperado. Verifique a declaração de sua função e certifique-se de retornar um valor do mesmo tipo declarado como retorno da função."""
        except:
            return ""


    def fieldIncompleteTypeFunc(self):
        try:
            typ = self.msg.split("field")[1]
            type1 = typ.split("has")[0]
            return """Tipo"""+type1+"""não reconhecido. Esse erro geralmente acontece quando o programador utiliza mais de um arquivo .c no seu código. Assim, a definição de uma estrutura que está em um arquivo.c não é reconhecida por outro .c. Para corrigir o erro da forma mais simples utilize apenas um arquivo.c e coloque todas as definições nele, caso contrário, inclua a definição de"""+type1+"""no arquivo .h (cabeçalho (header)) correspondente e inclua esse .h (#include "arquivo.h") em todos os programas .c que utilizarem esse tipo."""
        except:
            return ""
        

    def parameterIncompleteTypeFunc(self):
        return """Esse tipo de erro é um erro de cabeçalho (header) e geralmente está relacionado com o uso do 'typedef'. Verifique se você o está usando corretamente."""


    def fixedPointsTypesFunc(self):
        return """Esse tipo de número não é permitido nesse caso. Verifique se você não digitou um 'r', R', 'k' ou 'K' a mais no número e retire-o. Se sua intenção era fazer uma multiplicação de um número*R ou número*K, verifique se você não esqueceu do '*'."""


    def incompatibleTypesInitializingFunc(self):
        try:
            typ = self.msg.split("type")
            type1 = typ[2].replace("using", "").strip(" ")
            type2 = typ[3]
            return """Você está inicializando uma variável do tipo """+type1+""" com um valor do tipo"""+type2+""". Certifique-se de inicializar variáveis com valores que correspondem ao seu tipo de declaração."""
        except:
            return ""    
        
    
    def expectedTokensAtEndFunc(self):
        return """Verifique se não está faltando um '=' (igual), ',' (vírgula) ou ';' (ponto e vírgula) no final da linha."""    
            
    
    def expectedExpressionBeforeFunc(self):
        try:
            token = self.msg.split("before")[1]
            tok = token.split("token")[0].strip(" ")
            return """Antes do """+tok+""" tem que haver uma expressão. Para corrigir o erro certifique-se de colocar alguma expressão, que pode ser uma variável ou constante literal. Verifique ainda se não cometeu um erro de digitação ou se fez mau uso de algum comando da linguagem C."""    
        except:
            return ""


    def expectedDeclarationOrBeforeFunc(self):       
        return """Verifique no seu código se o número de chaves "{}" e parênteses "()" é par, verifique ainda se você está usando corretamente vírgulas, pontos e vírgulas e declarando variáveis corretamente."""    
    
    
    def expectedIdentifierOrBeforeFunc(self):
        try:
            tok = self.msg.split("or ")[1]
            tok = tok.split("before")[0]
            tok2 = self.msg.split("token")[0]
            tok2 = tok2.split("before")[1]
            return """Espera-se um identificador (nome dado a uma variável, função ou constante) ou um """+tok+"""antes do"""+tok2+""". Coloque-o para corrigir o erro. Verifique ainda se não cometeu um erro de digitação ou se fez mau uso de algum comando da linguagem C."""
        except:
            return ""

    
    def expectedTokensBeforeFunc(self):
        try:
            palavra = self.msg.split("before")[1]
            word = ""
            if "numeric constant" in palavra:
                word = "do número"
            elif "string constant" in palavra:
                word = "da string"
            else:
                word = "de " + palavra.replace("token", "").strip(" ")
            return """Verifique se não está faltando um '=' (igual), ',' (vírgula) ou ';' (ponto e vírgula) antes """+word+"""."""
        except:
            return ""
    

    
    def declarationStatementAtEndFunc(self):
        return """Geralmente esse erro ocorre quando está faltando um '}' em alguma parte do código. Verifique se seu código possui um número par de chaves (incluindo '{' e '}'), pois toda chave que você abre, você deve fechar."""    
            

    def expectedStatementBeforeFunc(self):
        try:
            token = self.msg.split("before")[1]
            tok = token.split("token")[0]
            return """Verifique se você não esqueceu de alguma declaração antes do"""+tok+"""ou se não cometeu algum erro de digitação nessa linha de código, como a utilização incorreta de parênteses. Lembre-se de contar os parênteses de forma que você tenha um número par deles, pois todo parêntese que você abre, você deve fechar."""  
        except:
            return ""
    
    
    def expectedDeclarationBeforeFunc(self):
        try:
            word = self.msg.split("before")[1]
            return """É esperada alguma declaração antes de"""+word+"""."""
        except:
            return ""
    
    
    def expectedToken1OrToken2Func(self):
        try:
            token1 = self.msg.split(" or ")[0]
            tok1 = token1.split("expected")[1]
            token2 = self.msg.split(" or ")[1]
            tok2 = token2.split("before")[0]
            comand = self.msg.split("before")[1]
            comando = ""
            if "numeric constant" in comand:
                comando = "do número"
            elif "string constant" in comand:
                comando = "da string"
            else:
                comando = "de" + comand.replace("token", "")
            return """Espera-se"""+tok1+""" ou """+tok2+"""antes """+comando+""". Coloque-o para corrigir o erro. Verifique ainda se não cometeu um erro de digitação ou se fez mau uso de algum comando da linguagem C."""
        except:
            return ""
    
        
    def expectedIdentifierBeforeFunc(self):
        try:
            token = self.msg.split("before")[1]
            tok = ""
            if "numeric constant" in token:
                tok = "do número"
            elif "string constant" in token:
                tok = "da string"
            else:
                tok = "de " + token.replace("token", "").strip(" ")
            return """Espera-se um identificador (nome dado a uma variável, função ou constante) antes """+tok+""". Coloque-o para corrigir o erro. Verifique ainda se não cometeu um erro de digitação ou se fez mau uso de algum comando da linguagem C."""
        except:
            return ""
        
        
    def expectedDeclarationOrAtEndFunc(self):
        return """Está faltando algum especificador no final da linha. Verifique no seu código se o número  de chaves "{}" e parênteses "()" é par, verifique ainda se você está usando corretamente vírgulas, pontos e vírgulas e declarando variáveis corretamente."""
        
        
    def expectedTokenAtEndFunc(self):
        try:
            token = self.msg.split("expected")[1]
            tok = token.split("at")[0]
            return """Verifique se não está faltando um"""+tok+"""no final da linha. Verifique ainda se não cometeu um erro de digitação ou se fez mau uso de algum comando da linguagem C."""
        except:
            return ""
        
        
    def expectedTokenIdentOrBeforeFunc(self):
        try:
            token1 = self.msg.split("expected")[1]
            tok1 = token1.split(",")[0]
            token2 = self.msg.split(" or ")[1]
            tok2 = token2.split("before")[0]
            word = self.msg.split("before")[1]
            return """Espera-se"""+tok1+""", um identificador (nome dado a uma variável, função ou constante) ou um """+tok2+"""antes de"""+word+""". Coloque-o para corrigir o erro. Verifique ainda se não cometeu um erro de digitação ou se fez mau uso de algum comando da linguagem C."""
        except:
            return ""


    def expectedSpecifierQualifierFunc(self):
        try:
            return """Verifique se você não esqueceu de colocar a palavra 'struct' antes da declaração de"""+self.msg.split("before")[1]+"""."""
        except:
            return ""    
        
        
    def expectedToken1BeforeToken2Func(self):
        try:
            token1 = self.msg.split("before")[0]
            tok1 = token1.split("expected")[1]
            token2 = self.msg.split("before")[1]
            tok2 = ""
            if "numeric constant" in token2:
                tok2 = "do número"
            elif "string constant" in token2:
                tok2 = "da string"
            else:
                tok2 = "de"+token2.split(" token")[0]      
            return """É esperado um"""+tok1+"""antes """+tok2+""". Coloque o"""+tok1+"""para corrigir o erro. Verifique ainda se não cometeu um erro de digitação ou se fez mau uso de algum comando da linguagem C."""
        except:
            return ""
    
    
    def strayInProgramFunc(self):    
        return """Verifique se você está usando algum caractere que não pertence à tabela ASCII, como ç, ã, é, ê, aspas diferentes, outre outros, ou algum caractere como '\\' ou '#' de forma incorreta e retire-o do código para corrigir o erro."""
        
    
    def elseWithoutIfFunc(self):
        return """Comandos 'else' só podem ser usados se houver um 'if' declarado anteriormente. Verifique se você declarou um 'if' antes de usar 'else' e verifique também se você está usando chaves "{}" corretamente para marcar os escopos desses condicionais."""    
    
    
    def missingTerminatingCharFunc(self):
        try:
            char = self.msg.split("terminating")[1]
            character = char.split("character")[0].strip(" ")
            return """Está faltando o caractere: """+character+""". Certifique-se de colocá-lo para corrigir o erro."""    
        except:
            return ""

    
    def valueRequiredAsLeftFunc(self):
        return """Se você estiver tentando fazer uma comparação certifique-se de usar os operadores de comparação corretamente, como '==' ao invés de '=' ou '!=' ou invés de '=!'. E se você estiver fazendo uma atribuição, certifique-se de deixar do lado esquerdo da igualdade a variável que vai receber o valor passado do lado direito, exemplo: x = a + b, ao invés de a + b = x."""

    
    def storageClassSpecifiedFunc(self):
        return """Esse tipo de erro é um erro de cabeçalho (header). Esse erro geralmente acontece quando um ";" (ponto e vírgula) é esquecido no final de alguma linha do arquivo.h em questão."""

    
    def breakNotWithinLoopFunc(self):
        return """O comando 'break' serve para parar imediatamente o laço e fazer o programa continuar após o laço. Ele só pode ser usado dentro de loops/laços e do switch. Verifique se você o está usando em uma dessas duas situações e se está demarcando o escopo do loop ou do switch corretamente com chaves "{}"."""    

    
    def invalidSuffixFunc(self):
        try:
            nome = self.msg.split("suffix")[1]
            name = nome.split("on")[0]
            return """Verifique se você digitou o nome"""+name+"""corretamente. Lembre-se de que nome de variáveis na linguagem C não podem começar com números. Obs: se você está tentando fazer uma multiplicação, então utilize '*'."""    
        except:
            return ""
    

    def caseNotWithinSwitchFunc(self):
        return """Verifique se você está usando 'case' dentro de um 'switch' e se está demarcando o escopo do switch corretamente com chaves "{}"."""    
    
    
    def initializerNotConstantFunc(self):
        return """Esse erro geralmente acontece quando o programador tenta declarar uma variável global e inicializá-la na sua declaração. Para corrigir o erro tente inicializar a variável apenas na função principal (main) e não na sua declaração."""
    
    
    def valueRequiredAsUnaryFunc(self):
        return """O operador unário '&' espera uma variável e não uma função, nem um número ou operações entre variáveis (exemplo: &(var1+var2)). Certifique-se de passar uma única variável, exemplo: &var."""
    
    
    def valueRequiredAsIncrementFunc(self):
        return """Algum valor é requerido como operando para incrementar. Incrementar um valor significa fazer: valor = valor + 1, logo, tente usar uma variável do tipo inteiro para realizar o incremento. Obs: o incremento pode ser escrito como valor++ ou ++valor."""
    
    
    def emptyCharacterConstantFunc(self):
        return """Caractere vazio. Se você quer atribuir vazio a uma string (vetor de caracteres), tente usar "" ou '\\0'."""
        
    
    def invalidDigitInOctalFunc(self):
        try:
            numero = self.msg.split("digit")[1]
            number = numero.split("in")[0].strip(" ")
            return """Em C geralmente um número iniciado com zero é entendido como um número octal, isto é, um número de base 8. Portanto, o compilador só reconhece os dígitos 0, 1, 2, 3, 4, 5, 6 e 7. Para corrigir esse erro, retire o zero da frente do número """+number+""". Porém, se o seu erro é porque você está tentando usar um número decimal, lembre que em C usamos "." (ponto) ao invés de "," (vírgula), exemplo: 0.0123 ou invés de 0,0123."""
        except:
            return ""
        
        
    def caseNotReduceToIntegerFunc(self):
        return """Label 'case' deve conter um valor constante. Se você quer utilizar condicionais com valores variáveis, utilize o 'if' no lugar do 'case'."""
        
        
    def labelUsedButNotDefinedFunc(self):
        try:
            lab = self.msg.split("label")[1]
            label = lab.split("used")[0].strip(" ")
            return """Se você estiver fazendo alguma comparação com """+label+""" certifique-se de que a comparação está completa e correta. Verifique ainda se você não está usando "&" de forma incorreta próximo a """+label+""", e se você estiver usando parênteses nesse trecho de código, certifique-se de que não está faltando nenhum."""
        except:
            return ""
        
        
    def forwardDeclarationFunc(self):
        return """Você está usando ";" (ponto e vírgula) onde deveria estar usando "," (vírgula). Lembre-se de que os parâmetros de funções em C são separados por vírgulas. Assim, para corrigir o erro substitua os pontos e vírgulas por vírgulas."""
                
        
    def tooManyDecimalPointsFunc(self):
        return """Existem muitos pontos decimais no número. Para consertar o erro, retire-os."""
        

    def macroMustBeIdentifierFunc(self):
        return """O nome do macro deve ser uma palavra."""


    def switchQuantityNotIntFunc(self):
        return """O argumento do 'switch' deve ser do tipo inteiro ou char."""


    def defaultNotWithinSwitchFunc(self):
        return """Label 'default' não está dentro do 'switch'. Certifque-se de não usar ';' (ponto e vírgula) depois do 'switch' e sim "{}" (chaves)."""
    

    def exponentHasNoDigitsFunc(self):
        return """Expoente não tem dígitos."""
    

    def unterminatedCommentFunc(self):
        return """Comentário não terminado. Lembre-se de que em C existem duas formas de comentar o código: usando '//' para comentar uma linha e usando /*comentario aqui*/, onde o /* marca o início do comentário e */ marca o final, sendo que nesse segundo caso o comentário pode se estender por mais de uma linha."""
        

    def valueRequiredAsDecrementFunc(self):
        return """Algum valor é requerido como operando para decrementar. Decrementar um valor significa fazer: valor = valor - 1, logo, tente usar uma variável do tipo inteiro para realizar o decremento. Obs: o decremento pode ser escrito como valor-- ou --valor"""


    def labelAtEndOfCompoundFunc(self):
        return """Uma label não pode ser vazia, logo, você deve colocar um "break;" ou apenas um ';' para consertar o erro."""
    

    def labelCanOnlyBePartOfStatementFunc(self):
        return """Esse erro geralmente ocorre quando há uma tentativa de declaração de variável dentro de um 'case'. Para corrigir o erro utilize chaves "{}" para demarcar o escopo do case, exemplo: case 1: { código } ou declare a variável em questão fora do case."""
    

    def noFollowingHexDigitsFunc(self):
        return """'x' na linguagem C é usado para trabalhar com número hexadecimais. Verifique se você está usando hexadecimais corretamente, e se o que você está tentando fazer é quebrar uma linha em C, lembre-se de que utilizamos '\\n' e não '\\x'."""
        

    def duplicateCaseValueFunc(self):
        return """Label 'case' deve conter um valor constante. Se você quiser utilizar condicionais com valores variáveis, então utilize o 'if' no lugar do 'case'."""
        

    def previouslyUsedHereFunc(self):
        return """Previamente declarado aqui."""
    

    def parameterNameOmittedFunc(self):
        return """Nome do parâmetro omitido. Você está especificando o tipo do parâmetro como argumento na função (exemplo: int, char, double) mas não está especificando o nome do parâmetro (exemplo: int nome, char nome). Certifique-se de especificar o tipo e o nome como argumento da função em questão."""
        

    def continueNotWithinLoopFunc(self):
        return """O comando 'continue' só pode ser usado dentro de loops/laços. Verifique se você o está usando nessa situação e se está demarcando o escopo do loop corretamente com chaves "{}"."""


    def duplicateLabelFunc(self):
        try:
            return """Label"""+self.msg.split("label")[1]+""" duplicada. Em C ':' (dois pontos) é usado depois de um nome para indicar que esse nome é uma label. Certifique-se de usar nomes diferentes na declaração de variáveis e labels."""
        except:
            return ""


    def nearInitializationFunc(self):
        try:
            return """A inicialização invalida de """+self.msg.split("for ")[1].replace(")","").strip(" ")+""" aconteceu próximo daqui."""
        except:
            return ""


    def duplicateWordFunc(self):
        try:
            return """'short' duplicado. Para consertar o erro apague um"""+self.msg.split("duplicate")[1]+"""."""
        except:
            return ""


    def mayNotAppearInMacroFunc(self):
        try:
            tok = self.msg.split("may")[0]
            return """Não é permitido """+tok+"""no nome do macro em questão. Remova o(s) """+tok+"""para consertar o erro."""
        except:
            return ""


    def duplicateMemberFunc(self):
        try:
            return """O membro"""+self.msg.split("member")[1]+""" está duplicado."""
        except:
            return ""


    def jumpIntoScopeOfIdentifierFunc(self):
        return """O comando 'goto' costuma tornar o código confuso, além disso, ele não é necessário e pode ser substituído por outras estruturas de controle, logo, a utilização do 'goto' não é recomendada. Dessa forma, tente reescrever o seu código sem fazer uso desse comando."""
     
    
    def subscriptNotIntegerFunc(self):
        return """O índice do array não é do tipo inteiro. Lembre-se de que na linguagem C os vetores possuem índices que vão de [0], [1], ... até o [TAMANHO-1], e logo, só podem ser do tipo 'int'."""
    
    def notAstructureOrUnionFunc(self):
        try:
            member = self.msg.split("member")[1]
            membro = member.split("in")[0]
            return """Você está tentando acessar"""+membro+"""como se fosse um membro de uma estrutura (registro/struct), mas não é. Verifique se você está usando as estruturas corretamente de acordo com a linguagem C. Lembrando que ao usar operadores como "." (ponto) e "->" é necessário que o operando do lado esquerdo seja uma estrutura, como um registro/struct, e o operando do lado direito seja um membro deste registro."""    
        except:
            return ""
    
    
    def neitherArrayNorPointerFunc(self):
        return """Você está tentando acessar uma posição de uma variável que não possui posições. Lembre-se de que para acessar posições de uma variável em C, essa variável precisa ser um vetor (exemplo: int vetor[10]) ou um ponteiro com algum tamanho alocado."""    
    
    def hasNoMemberNamedFunc(self):
        try:
            structure = self.msg.split("has")[0]
            membro = self.msg.split("named")[1]
            return structure+"""não possui nenhum membro/campo chamado"""+membro+"""."""
        except:
            return ""

    
    def arraySizeMissingFunc(self):
        try:
            array = self.msg.split(" in ")[1]
            return """Está faltando o tamanho do vetor """+array+""". Ao declarar um vetor em C você precisa especificar o tamanho dele. Por exemplo, para definir um vetor de tamanho 10, use int array[10]; Se for bidimensional você precisa especificar o tamanho das duas dimensões, exemplo: int array [10][20]; Lembre-se, na declaração de ponteiros não precisa colocar colchetes, mesmo que ele venha a ter posições, por exemplo: char *ponteiro; e não char *ponteiro[];"""
        except:
            return ""


    
    def incompleteElementTypeFunc(self):
        return """O vetor está incompleto. Certifique-se de especificar o tamanho das duas dimensões se você estiver trabalhando com um vetor bidimensional, por exemplo, int vetor[10][20], ou se você estiver trabalhando com um registro/struct e utilizou 'typedef' para defini-lo, certifique-se de não usar mais a palavra 'struct' quando declarar um objeto desse tipo."""    
    
    def variableSizedObjectFunc(self):
        return """Não é permitido inicializar objetos de tamanho variável em C dessa forma. Para corrigir esse problema você pode utilizar o 'memset' que inicializa cada posição do vetor com o valor que você desejar, por exemplo: memset(vetor, 0, sizeof(vetor)); para inicializar todas as posição de 'vetor' com o valor 0. Obs: Não esqueça de incluir a diretiva #include <string.h> no início do seu programa para utilizar a função 'memset'."""    
    

    def sizeNoIntegerTypeFunc(self):
        try:
            array = self.msg.split("array")[1]
            vetor = array.split("has")[0]
            return """O tamanho do vetor"""+vetor+"""não é do tipo inteiro. Corrija o erro atribuindo um valor inteiro como tamanho desse vetor."""
        except:
            return ""
    
    
    def invalidInitializerFunc(self):
        return """Inicialização inválida. Para inicializar valores de um vetor sem especificar seu tamanho utilize chaves "{}", por exemplo: int vetor[] = {1, 2, 3, 4}. Para inicializar valores de um vetor com tamanho especificado você precisa inicializar um por um dos índices. Para isso, você pode utilizar as chaves (explicadas acima), o comando 'memset' ou um laço 'for'. Se o vetor que você está tentando inicializar é uma string, então utilize aspas duplas, por exemplo: char string[10] = "Jaine". Por fim, se você está tentando inicializar um registro/struct, lembre-se de que deve você inicializar membro por membro."""
    
    
    def modifiedAtFileScopeFunc(self):
        try:
            array = self.msg.split("modified")[1]
            vetor = array.split("at")[0]
            return """Não é permitido na linguagem C atribuir um valor variável como tamanho de um vetor, pois os vetores devem possuir tamanho fixo, constante. Para isso, você pode substituir a variável utilizada no tamanho do vetor"""+vetor+"""por uma constante usando a diretiva #define NOME valor (por exemplo: #define TAMANHO 15) e assim utilizá-la como tamanho do seu vetor (por exemplo: int vetor[TAMANHO]). Ao usar uma constante, fica fácil alterar o tamanho do array em tempo de compilação, mas lembre-se de que o tamanho não muda durante a execução do programa."""
        except:
            return ""
    
    
    def flexibleArrayMemberFunc(self):
        try:
            return """Na linguagem C vetores declarados como membros de registros/structs devem ter seus tamanhos especificados. A exceção dessa regra se chama "membro vetor flexível" (exemplo de vetor flexível: int array[] - não tem tamanho especificado dentro dos colchetes) e você pode apenas ter um membro vetor flexível em um registro/struct, e esse membro deve ser sempre o último do registro. Portanto, para corrigir esse erro especifique o tamanho dos seus vetores ou declare-os como ponteiros, lembrando que só o último membro do registro pode ser um vetor flexível, ou seja, sem especificação de tamanho."""
        except:
            return ""
    
    
    def sizeTooLargeFunc(self):
        try:
            array = self.msg.split("array")[1]
            vetor = array.split("is")[0]
            return """O tamanho especificado para o vetor"""+vetor+"""é muito grande. Tente especificar um tamanho menor."""
        except:
            return ""
        
    
    def storageSizeNotKnownFunc(self):
        try:
            structure = self.msg.split("of")[1]
            estrutura = structure.split("isn’t")[0].strip(" ")
            return """Você está usando a palavra-chave 'struct' na declaração de"""+estrutura+"""embora não seja necessário, pois você utilizou 'typedef' para definir esse registro/struct como um tipo. Logo, para corrigir o erro remova a palavra 'struct' da declaração de """+estrutura+"""."""
        except:
            return ""
        
        
    def scalarIsRequiredFunc(self):
        try:
            return """Você usou um valor do tipo struct/registro onde um escalar é requerido."""
        except:
            return ""

        
    def invalidPreprocessingDirectiveFunc(self):
        try:
            diretiva = self.msg.split("directive")[1]       
            return """Erro no pré-processamento da diretiva"""+diretiva+""". A linguagem C possui diretivas que se iniciam com '#', como: #include para importar bibliotecas, #define para definir constantes ou trechos fixos de código, entre outras. Verifique se você digitou o nome dessas diretivas corretamente e com letras minúsculas."""
        except:
            return """"""
        
    
    def includeExpectsFunc(self):
        return """A diretiva #include espera o nome da biblioteca entre " " ou entre < >, por exemplo: #include "stdio.h" ou #include <stdio.h>. Verifique se você colocou em um desses dois formatos."""    
    
    def emptyFilenameFunc(self):
        return """Nome de arquivo vazio no #include. Verifique se você está usando um dos dois formatos adequados: #include <FILENAME> ou #include "FILENAME"."""    

    
    def noMacroNameGivenFunc(self):
        return """Nenhuma constante ou nenhum trecho de código foi definido na diretiva #define. Certfifique-se de definir isso, como no exemplo: #define CONSTANTE 10;"""
    
    
    def loopInitialDeclarationsFunc(self):
        return """A declaração de variáveis dentro de laços 'for', por exemplo: for(int i = 0; i < n; i++), não é permitida nesse padrão da linguagem C. Na versão "C99" da linguagem é que a declaração dentro da inicialização do for passou a ser permitida. Para resolver o erro declare a variável fora do loop 'for', por exemplo: int i; e for(i = 0; i < n; i++)."""


    def tooLongForGCCFunc(self):
        return """'long long long' não é permitido pelo compilador da linguagem C. Se você precisa usar um tipo para números muito grandes tente usar o 'double' ou o 'long double'."""

    '''
    
    def (self):
        return """ """    
    
    '''

    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.calledObjectNotFunction, self.tooFewArguments, self.tooManyArguments, 
                self.staticFollowsNoStatic, self.nestedFunction, self.voidValueNotIgnored, self.requireMoreArguments, 
                self.requireLessArgument, self.invalideUseOfVoid, self.oldStyleDeclaration, self.invalidStorageClass, 
                self.bracedGroup, self.initializedAsVariable, self.protypeDeclaration, self.numberArgumentsDoesntMatch,
                self.argumentDoesntMatchPrototype, self.undeclaredFirstUse, 
                self.declarationButNoParameter, self.redefinitionOfVariable, self.redeclarationOfVariable, 
                self.addressOfRegister,self.undeclaredHere, self.parameterIsInitialized, 
                self.redeclaredAsDifferentSymbol, self.declaredVoid, self.assignmentOfReadOnly, 
                self.decrementOfReadOnly, self.incrementOfReadOnly, self.unknownTypeName, self.invalidOperandsToBinary, 
                self.invalidTypeArgument, self.conflictingTypes, self.incompatibleTypesAssigning,self.incompatibleTypeArgument, 
                self.dereferencingPointer, self.invalidTypeOfUnary, self.typeFormalParameter, self.twoOrMoreDataTypes, 
                self.bothInDeclaration, self.invalidUseOfUndefined, self.invalidApplication, 
                self.conversionToNoScalar, self.incompatibleTypesReturning, self.parameterIncompleteType,
                self.fixedPointsTypes, self.incompatibleTypesInitializing, self.fieldIncompleteType,
                self.expectedTokensAtEnd, self.expectedExpressionBefore, self.expectedIdentifierOrBefore, 
                self.expectedTokensBefore, self.expectedDeclarationOrAtEnd, self.declarationStatementAtEnd, 
                self.expectedStatementBefore, self.expectedDeclarationBefore, self.expectedToken1OrToken2, 
                self.expectedIdentifierBefore, self.expectedDeclarationOrBefore, self.expectedTokenAtEnd, 
                self.expectedTokenIdentOrBefore, self.expectedSpecifierQualifier,  self.expectedToken1BeforeToken2,
                self.strayInProgram, self.elseWithoutIf, self.missingTerminatingChar, self.valueRequiredAsLeft, 
                self.storageClassSpecified,self.breakNotWithinLoop, self.invalidSuffix, self.caseNotWithinSwitch, 
                self.initializerNotConstant, self.valueRequiredAsUnary, self.valueRequiredAsIncrement, self.emptyCharacterConstant, 
                self.invalidDigitInOctal, self.caseNotReduceToInteger, self.labelUsedButNotDefined, self.forwardDeclaration, 
                self.tooManyDecimalPoints, self.macroMustBeIdentifier, self.switchQuantityNotInt, self.defaultNotWithinSwitch, 
                self.exponentHasNoDigits, self.unterminatedComment, self.valueRequiredAsDecrement, self.labelAtEndOfCompound, 
                self.labelCanOnlyBePartOfStatement, self.noFollowingHexDigits, self.duplicateCaseValue, self.previouslyUsedHere, 
                self.parameterNameOmitted, self.continueNotWithinLoop, self.duplicateLabel, self.nearInitialization, 
                self.duplicateWord, self.mayNotAppearInMacro, self.duplicateMember, self.jumpIntoScopeOfIdentifier,
                self.subscriptNotInteger, self.notAstructureOrUnion, self.neitherArrayNorPointer, 
                self.hasNoMemberNamed, self.arraySizeMissing,self.incompleteElementType, self.variableSizedObject, 
                self.sizeNoIntegerType, self.invalidInitializer, self.modifiedAtFileScope, self.flexibleArrayMember, 
                self.sizeTooLarge, self.storageSizeNotKnown, self.scalarIsRequired, 
                self.invalidPreprocessingDirective, self.includeExpects, self.emptyFilename, self.noMacroNameGiven,
                self.loopInitialDeclarations, self.tooLongForGCC]}

    
