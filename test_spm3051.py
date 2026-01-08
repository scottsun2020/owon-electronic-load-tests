import pyvisa
import time
import csv
from datetime import datetime

rm = pyvisa.ResourceManager("@py")
inst = rm.open_resource("ASRL/dev/ttyUSB0::INSTR")

inst.baud_rate = 115200
inst.data_bits = 8
inst.parity = pyvisa.constants.Parity.none
inst.stop_bits = pyvisa.constants.StopBits.one
inst.flow_control = pyvisa.constants.VI_ASRL_FLOW_NONE
inst.write_termination = "\r\n"
inst.read_termination = "\n"
inst.timeout = 2000
print("IDN:", inst.query("*IDN?").strip())
inst.timeout = 2000


# Set multimeter function
inst.write("FUNC VOLT:DC")

with open("spm3051_voltage_log.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "voltage_V"])

    for _ in range(10):  # 100 samples
        v = inst.query("CONFigure?").strip()
        ts = datetime.now().isoformat()
        writer.writerow([ts, v])
        print(ts, v)
        time.sleep(1)  # 1-second interval
