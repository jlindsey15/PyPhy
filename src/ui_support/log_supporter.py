import os

class log_supporter:
    def startup(self):
        import imports
        initial_report ="""

*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
[Info] PyPhy started at %s. Running version %s, last modified %s. 
[Info] Software written by %s.
    
    [Action] imports successfully loaded.
    [Action] ui_support successfully loaded.
    """ % (imports.program_start_time, imports.software_version, imports.software_date_mod, imports.software_authors)
        
        self.logw.write(initial_report)
        del imports

    
    def action(self, action_information):
        report = "[Action] " + str(action_information + "\n")
        self.logw.write(report)
    
    def error(self, error_information):
        report = "[Error] " + str(error_information + "\n")
        self.logw.write(report)
        
    def __init__(self): 
        os.chdir('/Users/' + os.environ['USER'] + '/Desktop/PyPhy/src')
        self.logw = open('data/log.pyphy', 'a')
        self.startup()