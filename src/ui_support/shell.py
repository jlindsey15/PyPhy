from objects import *
from physics import *
from regions import *
from world import *
import log_support
import gui_interface

def shell():
    log_support.shell_startup()
    print "Running in shell. To exit, type 'exit'."
    
    while True:
        code_line = raw_input('>>>')
        
        if code_line == "exit":
            break
            

        try:
            exec(code_line)
            log_support.shell_command(code_line, False)
            
        except:
            print "[Error] Invalid code. Type 'exit' to exit shell."
            log_support.shell_command(code_line, True)
            
                
    