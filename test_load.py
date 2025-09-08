import pyvisa
import time
import warnings

#warnings.filterwarnings("ignore", message="GPIB library not found", category=UserWarning)


rm = pyvisa.ResourceManager('@py')

instruments = rm.list_resources()

#print(instruments)


load = rm.open_resource("ASRL/dev/ttyUSB0::INSTR")


load.baud_rate = 115200
load.data_bits = 8
load.parity = pyvisa.constants.Parity.none
load.stop_bits = pyvisa.constants.StopBits.one
load.write_termination = '\n'   
load.read_termination = '\n'
load.timeout = 5000  # milliseconds

# Test to print Identification number
print("IDN:", load.query("*IDN?").strip())

time.sleep(0.5)  

# Switch to remote control
load.write("SYST:REM")
print("Switched to Remote Control")
time.sleep(1)
# Set mode to CR (constant resistor), 200 Ohm
load.write("FUNC RES")
time.sleep(0.5)

# Set resistance rise slew rate to FAST
load.write("RES:SLEW:RISE SLOW")
print("Set rise slope to SLOW")

time.sleep(1)
# Turn load ON
load.write("INPUT ON")
print("INPUT ON")
time.sleep(1)

# Ramp from 100Ω to 500Ω in steps
start_res = 100
end_res = 200
step = 10
delay = 0.5  # seconds between steps

for res in range(start_res, end_res + 1, step):
    load.write(f"RES {res}")
    print(f"Set Resistance to: {res} Ω")
    time.sleep(delay)
    # Read measured voltage/current/power
    voltage = load.query("MEAS:VOLT?")
    current = load.query("MEAS:CURR?")
    power   = load.query("MEAS:POW?")

    print("Measured Voltage:", voltage.strip())
    print("Measured Current:", current.strip())
    print("Measured Power:  ", power.strip())
    time.sleep(delay)
#load.write("RES 200")


time.sleep(3)


# Read measured voltage/current/power
voltage = load.query("MEAS:VOLT?")
current = load.query("MEAS:CURR?")
power   = load.query("MEAS:POW?")

print("Measured Voltage:", voltage.strip())
print("Measured Current:", current.strip())
print("Measured Power:  ", power.strip())

time.sleep(5)
# Turn load OFF and return to local control

print("Measured Voltage:", load.query("MEAS:VOLT?"))
print("Measured Current:", load.query("MEAS:CURR?"))
print("Measured Power:  ", load.query("MEAS:POW?"))

time.sleep(1)
load.write("INPUT OFF")
load.write("SYST:LOC")

load.close()
