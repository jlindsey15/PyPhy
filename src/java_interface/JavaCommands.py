

class JavaCommands:

    def start_update(self):
        message = 'start update'
        j_interface.pyphy.send(message)

    def update(self, ID, x, y, z, width, height, depth, r1, r2, r3):
        message = 'update' + " " + str(ID) + " " + str(x)\
                               + " " + str(y) + " " + str(z) + " " \
                               + str(width) + " " + str(height) + " " \
                               + str(depth) + " " + str(r1) + " " = str(r2) \
                               + " " + str(r2) + " " + str(r3)
        j_interface.pyphy.send(message)

    def end_update(self):
        message = 'end update'
        j_interface.pyphy.send(message)

    def print_message(self, output):
        message = 'print ' + output
        j_interface.pyphy.send(message)

    def println message(self, output):
        message = 'println ' + output
        j_interface.pyphy.send(message)
