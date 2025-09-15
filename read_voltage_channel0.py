from smbus2 import SMBus
import time

# === CONFIGURATION ===
I2C_BUS = 1           # /dev/i2c-1
DEVICE_ADDR = 0x48    # Replace with your detected address

# === ADS7128 Registers (from datasheet) ===
CH0_VOLTAGE_REG = 0x10  # Register for Channel 0 result
CONFIG_REG = 0x20       # General config register (if needed)

def read_channel_0():
    with SMBus(I2C_BUS) as bus:
        # Initiate a single-shot conversion on CH0 (assuming default settings)
        # Note: Some versions require writing to config registers first

        # Small delay before read (ADS7128 internal timing)
        time.sleep(0.01)

        # Read 2 bytes from CH0 result register
        raw = bus.read_word_data(DEVICE_ADDR, CH0_VOLTAGE_REG)

        # Byte swap might be needed depending on endianness
        raw_swapped = ((raw & 0xFF) << 8) | ((raw >> 8) & 0xFF)

        # ADS7128 is 12-bit ADC
        adc_value = raw_swapped & 0x0FFF

        # Assuming full scale is 5V, calculate voltage
        voltage = (adc_value / 4095.0) * 5.0

        return voltage, adc_value

# === MAIN ===
if __name__ == "__main__":
    voltage, raw = read_channel_0()
    print(f"Channel 0 Raw ADC Value: {raw}")
    print(f"Channel 0 Voltage: {voltage:.3f} V")
