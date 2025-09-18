### How to add ADS7128/7138 into IIO subsystem on Raspberry Pi

## Step 1: Flash SD card from Raspberry Pi 6.1 to 6.12

# check the version

```
uname -a
Linux raspberrypi 6.12.34+rpt-rpi-2712
```

I acctually need Kernel version 6.16 which has ads7128 driver under device tree. 

## Step 2: Download ads7138.c driver and Compile it 

kernel source: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/ti-ads7138.c

# create a Makefile

```
obj-m += ti-ads7138.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
```


which means compile the current ads7138.c and create a module for ads7138/7128 in the modules folders

# Error Occurs (Kernel Versions)
When my kernel was 6.1, the errors appeared a lot due to call apis from an older version driver
However, to compile a ads7128.c file this time contains only one error which reflects the kernel version incompatible issue. 

```
$:~/ads7128-driver $ ls
Makefile        ti-ads7138.c    ti-ads7138.mod.c
modules.order   ti-ads7138.ko   ti-ads7138.mod.o
Module.symvers  ti-ads7138.mod  ti-ads7138.o
```


# comand to test single register read for ads7128, ads7138

After I turned the I2c on from Raspberry pi, then I should see the connect ads7128 by the i2cdetect command:

```
i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- -- 
10: -- -- -- 13 -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --                      
```

https://www.ti.com/lit/ds/symlink/ads7128.pdf?ts=1757480501071#%5B%7B%22num%22%3A631%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C0%2C558.2%2C0%5D

# command to set and get value from i2c 

```
$ i2cset -f -y 1 0x13 0x10 0x00
$ i2cget -f -y 1 0x13
0x81
$ i2cset -f -y 1 0x13 0x10 0x20
$ i2cget -f -y 1 0x13
0xf0
```

I used these commands to have iio folder appears but later when the iio device is connected, iio folder will appear automatically (probably)

```
 sudo modprobe industriali
 $ sudo modprobe iio_trig_sysf
 $ sudo modprobe iio_trig_hrtime
 $ lsmod | grep iio
 ```

```
iio_trig_hrtimer       16384  0
industrialio_sw_trigger    16384  1 iio_trig_hrtimer
iio_trig_sysfs         16384  0
industrialio           90112  2 iio_trig_hrtimer,iio_trig_sysfs
```

## create overlay file for ads7128.dts

add overlay file7128ads.dtbo into boot/overlays 

add overlay into boot/config.txt
```
[all]
dtoverlay=ads7128
dtoverlay=ads7138
```

## update current kernel version 6.1(not support ads7128) to 6.16

```
rivieh@raspberrypi:~ $ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- -- 
10: -- -- -- UU -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --                         
```
