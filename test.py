import pyvisa
import time
import warnings

#warnings.filterwarnings("ignore", message="GPIB library not found", category=UserWarning)

rm = pyvisa.ResourceManager('@py')

instruments = rm.list_resources()

#print(instruments)
psu = rm.open_resource("ASRL/dev/ttyUSB1::INSTR")

psu.baud_rate = 115200
psu.data_bits = 8
psu.parity = pyvisa.constants.Parity.none
psu.stop_bits = pyvisa.constants.StopBits.one
psu.write_termination = '\n'   
psu.read_termination = '\n'
psu.timeout = 5000  # milliseconds

# Test to print Identification number
print("IDN:", psu.query("*IDN?").strip())

time.sleep(0.5)  

#Set System to Remote Control
#psu.write("SYST:REM")

#Configuring the Device
print("Set Voltage to 25:", psu.write("VOLT 25"))
time.sleep(0.5)  
print("Set Current to 0.02:", psu.write("CURR 0.020"))
time.sleep(0.5)  

print("Set Voltage Limit to 40:", psu.write("VOLT:LIM 50"))
time.sleep(0.5)  

print("Set Current Limit to 2:", psu.write("CURR:LIM 2.5"))

#Set the OUTPUT ON
print("Set Output OFF",psu.write("OUTP OFF"))
time.sleep(1)
print("Set Output On",psu.write("OUTP ON"))

# Wait for device to stabilize before Measurement
time.sleep(1)  


# Measure output
#print("Measure All returned:", psu.query("MEAS:ALL:INFO?"))
print("Measured Voltage:", psu.query("MEAS:VOLT?"))
print("Measured Curent:", psu.query("MEAS:CURR?").strip())
time.sleep(0.5)  

print("Measured Power:", psu.query("MEAS:POW?").strip())
time.sleep(0.5)  

print("Curent Limit:", psu.query("CURR:LIM?").strip())
print("Voltage Limit:", psu.query("VOLT:LIM?").strip())


time.sleep(10)

print("Measured Curent:", psu.query("MEAS:CURR?").strip(), "A")
print("Measured Power:", psu.query("MEAS:POW?").strip(), "W")

# Wait for device to stabilize before Measurement
time.sleep(1) 
#Set the OUTPUT OFF
print("Set Output OFF",psu.write("OUTP OFF"))

#Set System to Local Control
print("Set the control to local:", psu.write("SYST:LOC"))

psu.close()

