import pyvisa as visa
import time

# visa.log_to_screen() #allows user to see the backend calls being made to the pyvisa class
#^^essentially a built in debugger tool for the pyvisa package


visa.ResourceManager('@py') #creates t2he backend of library in case it wasn't already created
rm = visa.ResourceManager()
print(rm)
device = rm.list_resources() #returns a tuple of the connected instruments
print(device) #*prints the Serial port as still being active for some reason?*

SI = rm.open_resource(device[1]) #opens GPIB port and assigns the instrument in address 5 to an pyvisa object

print(SI) #prints the type of item this program creates "GPIBInstrument at GPIB::5::INSTR"


SI.write('*IDN?')
time.sleep(1) #on top of the built in delay the pyvisa object has, added a one second delay (which should be more than enough) for the system to properly recognize the command.
name = SI.read()
print(name) #prints "TDKRF, SI-300 w/SCAN,0,3.25"

SI.write('SI:MENU') #changes screens, executes successfully
time.sleep(1)

#
SI.write('SI:CONFIG4:CH1') #module 4 is the x-axis as per the documentation provided to me by TDKRF
time.sleep(1)
SI.write('SI:CONFIG5:CH2') #module 5 is the y-axis
time.sleep(1)

SI.write('SI:CH1') #SHOULD change screen to go to X-Y positioner. FAILS
time.sleep(1)
print(SI.read()) #prints "INVALID CHANNEL"

SI.write('SI:Q:CH1') #SHOULD return which module channel 1 is connected to(module 4), but FAILS
time.sleep(1)
print(SI.read())  #prints "INVALID CHANNEL"




#below this line are more commands SI-300 can take, nothing of concern as of right now.
############################################################################

# SI.write('MC:GO+020:CH1')
# print(SI.query('MC:PP:CH1'))
# SI.write('SI:CONFIG5:CH2')
# SI.write('SI:MODULE')
# SI.query('SI:Q:CH1')
# SI.write('SI:CH1')

# SI.write('*IDN?')

#for some reason this now gives an error?

# SI.query('*IDN?')
# SI.query('*RST') #resets the device

# SI.query('SI:MODULE')
# SI.query('SI:MENU')

# SI.write('*IDN?\n')
# time.sleep(1)
# print(SI.read())

# print(SI.query('*IDN?'))
#
# while SI.query('*IDN?') != 'SI-300 System Interface': #theoretically should output name of equipment, "SI-300 System Interface"
#     {
#         print('Query failed')
#     }


#SI.query('SI:CONFIG4:CH1') #configures X-axis to Channel 1
#SI.query('SI:CONFIG5:CH2') #configures Y-axis to Channel 2

#SI.query('SI:CH1')

#SET POSITIONS
# SI.write('MC:CP+100.0:CH1')  #CHANNEL 1 IS THE X AXIS
# SI.write('SI:CH1') #SWITCHES BETWEEN THE DIFFERENT MODULES IN THE CHANNEL SPECIFIED

#SI.query('*RST') #RESETS THE ENTIRE SYSTEM INTERFACE CONTROLLER

#just making sure this works, original running test code.
# print(dir(visa))
