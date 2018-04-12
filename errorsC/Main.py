# -*- coding: utf-8 -*-

import re
import sys
from errorsC.Errors import Error
from errorsC.Notes import Note

class Main(object):
    type = ""
    msg = ""
    line = ""
    code = ""
    function = ""
    lib = ""
    note = ""
    
    def __init__(self, typ, msg, line, code, function, lib, note):
        self.type = typ
        self.msg = msg
        self.line = line
        self.code = code
        self.function = function
        self.lib = lib
        self.note = note
        
    def chainResponsability(self):   
        
        ''' Cadeia de Busca '''

        chain = ['Error(self.msg).getErros()']
              
              
        foundType = False #Se encontrar a classe do tipo
        foundMsg = False #Se encontrar a mensagem de erro
        
        listError = [] #lista dos erros ao identificar a classe
        
        '''
            Cadeia das classes de erros, verificando se algum casa com a entrada
            Caso case, é passado a lista de erros deste tipo
        
        '''
        retorno = []
        
        for i in chain:
            i = eval(i)
            if self.type in i:
                listError = i[self.type]
                foundType = True
                break           
                #continue #encerra a busca pela cadeira
                
        ''' Se encontrou o tipo do erro da entrada
            
            Cadeia de erros, verificando se algum da cadeia casa com a entrada
            Caso case, é chamado o método correspondente que transforma a mensagem de erro
            
        '''
    
        if foundType:
            for l in listError:
                for i in l.keys():
                    if i in self.msg:
                        if not self.function == "": retorno.append("Na função"+self.function+"\n")
                        if not self.lib == "": retorno.append("Na liblioteca "+self.lib+"\n")
                        retorno.append("Erro na linha "+self.line+"\n")
                        if not self.code == "": retorno.append("No trecho de código:\n")
                        retorno.append(self.code+"\n")
                        retorno.append("Descrição: "+l[i]+"\n")
                        if not self.note == "": retorno.append("\n"+"Nota: "+self.note)
                        retorno.append("\n")
                        foundMsg = True
                        break
                        #continue#encerra a busca pela cadeira
                if foundMsg:
                    break        
            if not foundMsg:
                #retorno.append("400")
                print (self.msg)
                retorno.append("Erro não encontrado!")
                
        else:
            #retorno.append("400")
            print( self.msg)                
            retorno.append("Tipo de erro não encontrado!")
            
        return ''.join(retorno)

   
def executeC(errorMsg):
    
    '''
        Carregando a mensagem de erro
    '''        
    
    list_begin = []
    
    ''' Separando a mensagem em linhas e identificando a linha que contém a string error
    filename = "..\\file\\baseErros.txt"
    with open(filename) as f:'''
    
    try:
        for line in errorMsg.split("\n"):
            list_begin.append(line)
    except Exception as e:
        print( errorMsg, sys.exc_info()[0], e)
        return "Mensagem de erro fora do padrão!"
        
    matriz_errors = []
    linha = []
    tam = len(list_begin)-1
    for i, line in enumerate(list_begin):
        try:
            linha.append(line)  
            if line.strip(" ") == "^":            #error com código fonte
                if i == tam:
                    matriz_errors.append(linha)
                    linha = []                                   
                if (not "note: " in list_begin[i+1]):
                    if not "In file included from" in list_begin[i+1]:
                        matriz_errors.append(linha)
                        linha = []                 
                    else:
                        if not "note: " in  list_begin[i+2] and not "note: " in  list_begin[i+3] and not "note: " in  list_begin[i+4] and not "note: " in  list_begin[i+5]:
                            matriz_errors.append(linha)
                            linha = []                                                        
            elif "error:" in line and i == tam:                       #error na ultima linha sem código fonte
                matriz_errors.append(linha)
                linha = []                               
            elif "error:" in line and list_begin[i+1][0] != " ":      #error sem código e sem ser na última linha   /Índice.c:21:8: error: ‘ind’
                if (not "note: " in list_begin[i+1]):
                    if not "In file included from" in list_begin[i+1]:
                        matriz_errors.append(linha)
                        linha = []                                                
                    else:
                        if not "note: " in  list_begin[i+2] and not "note: " in  list_begin[i+3] and not "note: " in  list_begin[i+4] and not "note: " in  list_begin[i+5]:
                            matriz_errors.append(linha)
                            linha = []                            
            elif "note:" in line:                                    #note /Cálculo.c:32:9: note: previous
                if i == tam or "error: " in list_begin[i+1] or "In function" in list_begin[i+1] or not list_begin[i+1]:
                    matriz_errors.append(linha)
                    linha = []     
        except IndexError:
            continue
    finalMsg = ""    
    if not matriz_errors:
        #return "400"
        print(errorMsg, sys.exc_info()[0])
        return "Mensagem de erro fora do padrão!"
    else:
        #print(matriz_errors) 
        for list_erros in matriz_errors:
            list_new = []
            #print(list_erros)
            
            ''' Separando o tipo do erro e sua mensagem '''
            for line in list_erros:
                if "error:" in line:
                    classError = "error"
                    list_new.append(classError)
                    message = line.split("error: ")[1]
                    list_new.append(message)
                    break
            
            
            ''' Pegando a função com erro '''
            func = []
            #print(list_begin)
            try:
                for line in list_erros:
                    if "In function" in line:
                        func.append(line.split("function")[1])
                str_func = ''.join(func)
            except:
                func = ""
                    
                    
            ''' Pegando a liblioteca com erro '''
            lib = []
            #print(list_begin)
            try:
                for line in list_erros:
                    if ".h:" in line and "error:" in line:
                        aux = line.split(".h:")[0]
                        aux = aux.split("/")
                        aux = aux[::-1][0]
                        lib.append(aux)
                str_lib = ''.join(lib)
            except:
                lib = ""
               
        
            ''' Pegando nota/aviso '''
                
            note = []     
            flag = False
            try:
                for line in list_erros:
                    if flag and not "note: " in line:
                        note.append(line+"\n")
                    if "note:" in line:
                        n = Note(line)
                        for i in n.dict.keys():
                            if i in line:
                                note.append(n.getNote(i)+"\n")
                                break
                        flag = True
                str_note = ''.join(note)
            except:
                note = ""   
                
                
            ''' Pegando o código fonte '''
            
            cod = []
            try:
                for i, line in enumerate(list_erros):
                    if line.strip(" ") == "^" and not "note:" in list_erros[i-2]:
                        trecho = list_erros[i-1]
                        cod.append(trecho+"\n")
                        cod.append(line+"\n")
                        break
                str_code = ''.join(cod)                  
            except:
                cod = ""
            
            
            ''' Pegando a linha que ocorreu o erro'''
            linha = ""
            for f in list_erros:
                try:
                    if ".c:" in f and "error:" in f or ".h:" in f and "error:" in f:       
                        linha = f          
                except:
                    continue
            
    
            ''' Identificando o número da linha que ocorreu o erro '''
            numberLine = ""
            try:
                l = linha.split(':')[1]
                if l.isdigit():
                    numberLine = l
                else:
                    numberLine = "X"
                ''' Executando a chamada da cadeia com o tipo do erro e sua mensagem'''
                
                '''print numberLine
                print str_code
                print list_new[0]+":"+list_new[1]'''
                
                iniciar = Main(list_new[0], list_new[1], numberLine, str_code, str_func, str_lib, str_note)
                finalMsg += iniciar.chainResponsability()
            except Exception as e:
                #return "400"
                print(errorMsg, sys.exc_info()[0], e)
                return "Mensagem de erro fora do padrão!"
        return finalMsg



