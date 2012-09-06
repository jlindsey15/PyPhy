#!/usr/bin/python


import imports
import ui_support

ui_support.log_support.error("TESTING ERRORS")


ui_support.log_support.startup()

import java_interface
import physics_interface
j_interface = java_interface.java_interface()

j_interface.pyphy.send("HI")

p_interface = physics_interface.physics_interface()