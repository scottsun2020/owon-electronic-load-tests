import os

IIO_PATH = "/sys/bus/iio/devices/iio:device0"

def read_scale():
    try:
        with open(os.path.join(IIO_PATH, "in_voltage_scale"), 'r') as f:
            return float(f.read().strip())
    except FileNotFoundError:
        print("Error: Global scale file not found.")
        return None

def read_raw(channel):
    try:
        with open(os.path.join(IIO_PATH, f"in_voltage{channel}_raw"), 'r') as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return None

def main():
    scale = read_scale()
    if scale is None:
        return

    print(f"Global Scale: {scale} mV/unit")

    # Read up to 8 channels (ADS7128 supports 8 analog inputs)
    for ch in range(8):
        raw = read_raw(ch)
        if raw is not None:
            voltage = raw * scale / 1000  # Convert mV to V
            print(f"Channel {ch}: Raw = {raw}, Voltage = {voltage:.3f} V")
        else:
            print(f"Channel {ch}: Not available")

if __name__ == "__main__":
    main()
