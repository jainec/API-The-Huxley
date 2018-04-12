import re
import sys
from errorsPython.nameError import NameE
from errorsPython.syntaxError import SyntaxE
from errorsPython.systemError import SystemE
from errorsPython.valueError import ValueE
from errorsPython.typeError import TypeE
from errorsPython.EOFError import EOFE
from errorsPython.indentationError import IndentationE
from errorsPython.indexError import IndexE
from errorsPython.attributeError import AttributeE
from errorsPython.keyError import KeyE
from errorsPython.unboundLocalError import UnboundLocalE
from errorsPython.fileNotFoundError import FileNotFoundE
from errorsPython.zeroDivisionError import ZeroDivisionE
from errorsPython.tabError import TabE
from errorsPython.importError import ImportE
from errorsPython.permissionError import PermissionE
from errorsPython.overflowError import OverflowE
from errorsPython.unicodeDecodeError import UnicodeDecodeE
from errorsPython.calendarIllegalMonthError import IllegalMonthE
from errorsPython.unicodeEncodeError import UnicodeEncodeE
from errorsPython.IOError import IOE
from errorsPython.main import executePython
from errorsC.Errors import Error
from errorsC.Notes import Note
from errorsC.Main import executeC
from bottle import run, post, request, debug


def checkMsg(msg):
    return (True if "\n" in msg and msg is not None else False)

@post('/')
def postMsg():
    try:
        errorMsg = request.forms.get('errorMsg')
        extension = request.forms.get('extension')
        if extension == ".c" and checkMsg(errorMsg):
            return executeC(errorMsg)
        elif extension == ".py" and checkMsg(errorMsg):
            return executePython(errorMsg)
        else:
            print(errorMsg)
            return "Mensagem de erro fora do padrão!"
    except Exception as e:
        print(errorMsg, sys.exc_info()[0], e)
        
if __name__ == '__main__':    
    debug(True)
    run(host='localhost', port=8080, debug=True, reloader=True)
    
    