import log_supporter

log_support = log_supporter.log_supporter()


#### RECONSIDER


            


def load_menu():
    print "Loading Saves"
    saves = []
    for filename in os.listdir('data'):
        if filename[-5:] == ".pyps":
            saves.append(filename)   
    
    print "Which save should be imported? (Type 'exit' to go back to previous menu.)"
    
    for save in saves:
        print str(saves.index(save)+1) + ". " + str(save)
        
    to_load = raw_input('')
    
    if to_load != "exit":
        
        try:
            to_load = int(to_load)
            ui_support.log_support.request("User requested " + saves[to_load - 1] + " to be loaded.")
            ui_support.load()
            print "Should have loaded."
        
        except:
            ui_support.log_support.error("User entered invalid load option in ui.py - load_menu(). Exited to main loop.")
            
        
        
    
    
    
    