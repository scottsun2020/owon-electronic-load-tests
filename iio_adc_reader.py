import os

# Adjust to match your actual IIO device path
IIO_DEVICE = "/sys/bus/iio/devices/iio:device0"

def read_voltage(channel):
    raw_path = f"{IIO_DEVICE}/in_voltage{channel}_raw"
    scale_path = f"{IIO_DEVICE}/in_voltage{channel}_scale"

    try:
        with open(raw_path, 'r') as f:
            raw = int(f.read().strip())
    except FileNotFoundError:
        print(f"[ERROR] Channel {channel} raw file not found.")
        return None

    try:
        with open(scale_path, 'r') as f:
            scale = float(f.read().strip())
    except FileNotFoundError:
        # If scale is not available, assume 1.0 (raw counts only)
        scale = 1.0

    voltage = raw * scale
    return voltage

# Example: Read channels 0 to 3
for ch in range(4):
    voltage = read_voltage(ch)
    if voltage is not None:
        print(f"Channel {ch}: {voltage:.3f} V")
