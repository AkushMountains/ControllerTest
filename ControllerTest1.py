import pyvisa as visa
import time
visa.log_to_screen() #allows user to see the backend calls being made to the pyvisa class

visa.ResourceManager('@py') #creates t2he backend of library in case it wasn't already created
rm = visa.ResourceManager()
print(rm)
device = rm.list_resources() #returns a tuple of the connected instruments
print(device)
#maybe add a line to verify the if ""== "main": ??


SI = rm.open_resource(device[1]) #opens GPIB port and assigns the instrument in address 5 to an pyvisa object
print(len(device)) #prints the number of devices connected to the laptop

print(SI) #prints the type of item this program creates

SI.write('*IDN?')
time.sleep(1)
name = SI.read()
print(name)

# SI.write('SI:MENU')
time.sleep(1)


SI.write('SI:CONFIG4:CH1')
# SI.write('MC:GO+020:CH1')
# print(SI.query('MC:PP:CH1'))
# SI.write('SI:CONFIG5:CH2')
# SI.write('SI:MODULE')
# SI.query('SI:Q:CH1')
# SI.write('SI:CH1')

#below this line is all the commands used to make the instrument do things, will cause error if python cannot communicate with the device
############################################################################

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
# SI.write('MC:RXA555:CH1') #SETS X AXIS RATIO TO +5.55
# SI.write('SI:CH1') #SWITCHES BETWEEN THE DIFFERENT MODULES IN THE CHANNEL SPECIFIED

#SI.query('*RST') #RESETS THE ENTIRE SYSTEM INTERFACE CONTROLLER

#just making sure this works, original running test code.
# print(dir(visa))
