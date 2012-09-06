import imports
import socket 
import ui_support




class pp_socket: 
    
    send_queue = []
    recv_queue = []
    
    def start(self):    
        time_to_try = 1
        while True:       
            try:
                self.pyphy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                host = '127.0.0.1'
                port = 5275              
                self.pyphy.connect((host, port))
                self.pyphy.settimeout(.00001)
                ui_support.log_support.action("Socket at port 5275 created.")
                break   
              
            except:
                print "[Error] Socket not established. Will retry in %s seconds." %time_to_try
                ui_support.log_support.error("Socket not established.")
                imports.py_time.sleep(time_to_try)
                
            if time_to_try == 16 or time_to_try == 30:
                time_to_try = 30           
            else:
                time_to_try *= 2
                
    
    
    
    def comm(self):
        while True: 
            while len(self.send_queue) != 0:
                message = self.send_queue.pop(0)
                print "Sending message:", message
                self.pyphy.sendall(message + "|nln|")

            try:
                data = self.pyphy.recv(1)
                if data != "":
                    while data[-5:] != "|nln|":
                        data += self.pyphy.recv(1)        
                    data = data[:len(data) - 5]
                    self.recv_queue.append(data)           
                    print "Received Message:", data
                        
                if data == "shutdown":
                    imports.sdc = True
                    
                data = ""
                    
            except:
                pass
            
            if imports.sdc == True:
                break
    
            
    def send(self, message):
        self.send_queue.append(message)
            
            
    def __init__(self):
        self.start()       
        communication_thread = imports.threading.Thread(target = self.comm, name = "Communication")
        communication_thread.start()

