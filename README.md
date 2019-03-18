# Thingy52 Snap

This snap contains the `bluepy` package as well as a helper utility script to find Thingy52 BLE devices.


## Building

To build, install snapcraft and multipass:

```bash
$ snap install snapcraft --classic
$ snap install multipass --classic --beta
```

Then build the snap with snapcraft:

```
$ git clone https://github.com/anonymouse64/thingy52-snap.git
$ cd thingy52
$ snapcraft
```

## Installing

After building the snap, install the snap with:

```bash
$ snap install --dangerous thingy52*.snap
```

The snap plugs `bluetooth-control` in order to talk with the BLE devices. This interface is not auto-connected, so after installation you must connect this interface manually with:

```bash
$ snap connect thingy52:bluetooth-control
```

## Using the snap

The main command is `thingy52` which is the same as the thingy52.py script shipped with `bluepy`:

```bash
$ sudo /snap/bin/thingy52 --help
usage: thingy52 [-h] [-n COUNT] [-t T] [--temperature] [--pressure]
                [--humidity] [--gas] [--color] [--keypress] [--tap]
                [--orientation] [--quaternion] [--stepcnt] [--rawdata]
                [--euler] [--rotation] [--heading] [--gravity] [--battery]
                [--speaker] [--microphone]
                mac_address

positional arguments:
  mac_address    MAC address of BLE peripheral

optional arguments:
  -h, --help     show this help message and exit
  -n COUNT       Number of times to loop data
  -t T           time between polling
  --temperature
  --pressure
  --humidity
  --gas
  --color
  --keypress
  --tap
  --orientation
  --quaternion
  --stepcnt
  --rawdata
  --euler
  --rotation
  --heading
  --gravity
  --battery
  --speaker
  --microphone
```

If you don't know the MAC address of your Thingy52 you can use the `find`, optionally specifying how long to scan for with the `--scantime` option and the name of the device to search for with `--name`. See:

```bash
$ sudo thingy52.find --name MyThingy
c2:fe:6a:0f:91:16
```

### Examples

Play a sound on the Thingy:

```bash
sudo thingy52 c2:fe:6a:0f:91:16 --speaker
```
