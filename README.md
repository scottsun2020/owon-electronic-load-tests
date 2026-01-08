# OWON Electronic Load Control Scripts

This repository contains Python scripts to communicate with the **OWON OEL1515 DC Electronic Load** using the SCPI protocol via USB serial connection (PyVISA).  
The scripts allow users to set operating modes (CR, CC, CV, CP), ramp resistance, and read measurements.

---

## 🔧 Requirements

- Python 3.10+
- [PyVISA](https://pyvisa.readthedocs.io/en/latest/)
- [PyVISA-py](https://pyvisa-py.readthedocs.io/)
- OWON OEL1515 DC Electronic Load
- USB-to-Serial connection

Install required packages in a virtual environment:

```bash
python3 -m venv pyvisa
source pyvisa/bin/activate
pip install pyvisa pyvisa-py
```

One thing to pay attention if the identification number not shows up, you may have to check these two lines on your script:
```
inst = rm.open_resource("ASRL/dev/ttyUSB0::INSTR")

inst.baud_rate = 115200
```

## Example of SPM3051
![spm3051](https://github.com/user-attachments/assets/96c95b5f-2348-409c-a583-0a795f79de76)

## Measurement from SPM3051

<img width="765" height="398" alt="Screenshot from 2026-01-08 13-51-25" src="https://github.com/user-attachments/assets/c9394474-5b10-4277-9356-58ad83188563" />

## CSV file output for timestamp and voltage measurement from SPM3051
<img width="944" height="519" alt="Screenshot from 2026-01-08 14-02-11" src="https://github.com/user-attachments/assets/62a7f78f-dcb5-4333-b5d9-a80c72baa2e4" />


