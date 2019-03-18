from bluepy import btle
import binascii
import argparse

# setup argument options
parser = argparse.ArgumentParser()
parser.add_argument('--name', help='Name of Thingy52 to search for', default="Thingy")
parser.add_argument('--scantime', help='How long to scan for devices', type=float, default=5)
args = parser.parse_args()

# scan for devices
scanner = btle.Scanner()
ble_devices = scanner.scan(timeout=args.scantime)

MAC_ADDRESS = None
for dev in ble_devices:
    for (adtype, desc, value) in dev.getScanData():
        # check if this device attribute data has type=9 (which is the name)
        # the same as the name provided in the args
        if (adtype == 9) and (value == args.name):
            print("{}".format(dev.addr))
            MAC_ADDRESS = dev.addr

# if we didn't find the device exit, exit non-zero and print message for easy
# scripting
if (MAC_ADDRESS == None):
    print("error: found no devices with name \"{}\"".format(args.name))
    exit(1)
