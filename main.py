# Type help("robodk.robolink") or help("robodk.robomath") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/robodk.html
# Note: It is not required to keep a copy of this file, your Python script is saved with your RDK project

# Libraries
from robodk import *      # RoboDK API
from robolink import *    # Robot toolbox

import socket
import struct
import math

## RTDE ##
import sys
sys.path.append(r'C:\RoboDK\Python')
import rtde.rtde as rtde
import rtde.rtde_config as rtde_config

## API provider ##
RDK = Robolink()

robot = RDK.Item("UR3e")
# RTDE connection
host = "192.168.234.130"
con = rtde.RTDE(host, 30004)
con.connect()

if not con.send_output_setup(["target_q"],["VECTOR6D"], frequency=30):
    sys.exit()

if not con.send_start():
    sys.exit()

try:
    while True:
        state = con.receive()
        if state is not None:
            robot.setJoints([x*180/math.pi for x in state.target_q])

except KeyboardInterrupt:
    pass

con.send_pause()
con.disconnect()
