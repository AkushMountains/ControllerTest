import pyvisa as visa
visa.log_to_screen()

rm = visa.ResourceManager()
visa.ResourceManager('@py') #creates t2he backend of library in case it wasn't already created
device = rm.list_resources() #returns a tuple of the connected instruments
print(device)
#maybe add a line to verify the if ""== "main": ??


SI = rm.open_resource(device[0]) #opens COM22 an assigns it as a serial port, "ASRL".. creates a PyVisa object.

print(SI) #prints the type of item this program creates

#below this line is all the commands used to make the instrument do things, well cause error if python cannot communicate with the device
############################################################################

# SI.write('*IDN?')

# SI.query('*IDN?')
# SI.query('*RST') #resets the device


SI.query('SI:MODULE')
# SI.query('SI:MENU')

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
# SI.write('MC:RXA555:CH1') #SETS X AXIS RATIO TO +5.55
# SI.write('SI:CH1') #SWITCHES BETWEEN THE DIFFERENT MODULES IN THE CHANNEL SPECIFIED

#SI.query('*RST') #RESETS THE ENTIRE SYSTEM INTERFACE CONTROLLER

#just making sure this works, original running test code.
# print(dir(visa))
# print(rm)::INSTR')
