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
